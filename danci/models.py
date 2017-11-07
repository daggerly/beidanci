#coding: utf-8
from __future__ import unicode_literals
from datetime import datetime, timedelta

from django.db import models
from django.utils.timezone import now as tznow

class Danci(models.Model):
    word = models.CharField(max_length=50, null=False, blank=False,
                            primary_key=True)
    meaning = models.CharField(max_length=50, null=False, blank=False)
    created_dt = models.DateTimeField(u'创建', auto_now_add=True)

    def __unicode__(self):
        return self.word


class AbstractRecord(models.Model):
    danci = models.ForeignKey(Danci, primary_key=True)
    corrected = models.PositiveSmallIntegerField(u'正确次数', default=0,)
    last_dt = models.DateTimeField(u'上次背', auto_now=True)
    next_dt = models.DateTimeField(u'下次背', auto_now_add=True)
    created_dt = models.DateTimeField(u'创建', auto_now_add=True)
    learned = models.BooleanField(u'掌握了', default=False)


    class Meta:
        ordering = ('-next_dt',)
        abstract = True

    def __unicode__(self):
        return unicode(self.danci)


    @staticmethod
    def get_next_show_dt(corrected):
        now = tznow()
        if corrected == 0:
            delta = timedelta(days=1)
        elif corrected == 1:
            delta = timedelta(days=3)
        elif corrected == 2:
            delta = timedelta(days=7)
        elif corrected == 3:
            delta = timedelta(days=30)
        else:
            delta = timedelta(days=30 * 6)
        return now + delta


    def unpassed(self):
        self.corrected = 0
        self.next_dt = self.get_next_show_dt(0)
        super(AbstractRecord, self).save()


    def passed(self):
        self.next_dt = self.get_next_show_dt(self.corrected)
        self.corrected += 1
        if self.already_learned():
            self.set_learned()
        else:
            super(AbstractRecord, self).save()


    def set_learned(self):
        if self.corrected < 10:
            raise Exception("You haven't study this word for 10 times, not sure you have already leaned!")
        self.learned = True
        super(AbstractRecord, self).save()


    def already_learned(self):
        return self.corrected >= 10

    @classmethod
    def get_word_to_learn(cls):
        """
        查找应该背的单词,先找背过的词,再找没背过的词
        :param mode:
        :return:
        """
        # 旧词
        record = cls.objects.filter(learned=False, next_dt__lte=tznow()) \
                .order_by('?').first()
        if record:
            return record.danci
        # 新词
        danci = Danci.objects.exclude(word__in=
                cls.objects.all().values_list('danci__word', flat=True)
                ).order_by('?').first()
        if danci:
            record = cls(danci=danci)
            record.save()
        return danci

class WordmodeRecord(AbstractRecord):
    class Meta:
        verbose_name = 'WordmodeRecord'
class MeaningmodeRecord(AbstractRecord):
    class Meta:
        verbose_name = 'MeaningmodeRecord'


RECORD_TYPES = {'WordmodeRecord': WordmodeRecord,
                'MeaningmodeRecord': MeaningmodeRecord}
