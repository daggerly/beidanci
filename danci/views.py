#coding: utf-8
from django.contrib import messages
from django.shortcuts import render_to_response, redirect

from danci.models import (WordmodeRecord, MeaningmodeRecord, Danci,
                          RECORD_TYPES)

def study_word(request):
    if request.method=='POST':
        word = request.POST['word']
        result = request.POST['result']
        word = WordmodeRecord.objects.get(danci__word=word)
        if result == 'pass':
            word.passed()
        elif result == 'unpass':
            word.unpassed()
    d = WordmodeRecord.get_word_to_learn()
    words_to_learn_number = WordmodeRecord.count_words_to_learn()
    return render_to_response('study_word.html',{'danci':d, 'WORDS_TO_LEARN_NUMBER': words_to_learn_number})

def study_meaning(request):
    if request.method=='POST':
        word = request.POST['word']
        result = request.POST['result']
        word = MeaningmodeRecord.objects.get(danci__word=word)
        if result == 'pass':
            word.passed()
        elif result == 'unpass':
            word.unpassed()
    d = MeaningmodeRecord.get_word_to_learn()
    words_to_learn_number = MeaningmodeRecord.count_words_to_learn()
    return render_to_response('study_meaning.html',{'danci':d, 'WORDS_TO_LEARN_NUMBER': words_to_learn_number})


def synchronize_new_words(request, name):
    record_model = RECORD_TYPES[name]
    exist_words = record_model.objects.all().values_list('danci__word', flat=True)
    new_words = Danci.objects.exclude(word__in=exist_words)
    if new_words:
        params = [record_model(danci=i) for i in new_words]
        record_model.objects.bulk_create(params)
        msg = '%d new words created' % len(params)
    else:
        msg = 'no more new words'
    messages.add_message(request, messages.INFO, msg)
    return redirect('admin:danci_%s_changelist'%name.lower())