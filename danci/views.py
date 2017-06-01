#coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse

from danci.models import ( WordmodeRecord, MeaningmodeRecord,
                          get_word_to_learn, WORD_MODE, MEANING_MODE)

def study_word(request):
    if request.method=='POST':
        word = request.POST['word']
        word = WordmodeRecord.objects.get(danci__word=word)
        if 'pass' in request.POST:
            word.passed()
        elif 'unpass' in request.POST:
            word.unpassed()
    d = get_word_to_learn(WORD_MODE)
    return render_to_response('study_word.html',{'danci':d})

def study_meaning(request):
    if request.method=='POST':
        word = request.POST['word']
        word = MeaningmodeRecord.objects.get(danci__word=word)
        if 'pass' in request.POST:
            word.passed()
        elif 'unpass' in request.POST:
            word.unpassed()
    d = get_word_to_learn(MEANING_MODE)
    return render_to_response('study_meaning.html',{'danci':d})

def add(request):
    return HttpResponse('use admin')
