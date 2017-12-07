from django.contrib import admin
from models import Danci, WordmodeRecord, MeaningmodeRecord

class DanciAdmin(admin.ModelAdmin):
    list_display = ('word', 'meaning', 'created_dt')
    ordering = ['-created_dt']
    search_fields = ['word']

class RecordAdmin(admin.ModelAdmin):
    list_display = ('danci', 'corrected', 'last_dt', 'next_dt', 'created_dt')
    ordering = ['next_dt']
    actions_on_top = False
    actions_on_bottom = True

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['WORDS_TO_LEARN_NUMBER'] = self.model.count_words_to_learn()
        return super(RecordAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(Danci, DanciAdmin)
admin.site.register(WordmodeRecord, RecordAdmin)
admin.site.register(MeaningmodeRecord, RecordAdmin)