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

class WordmodeRecordAdmin(RecordAdmin):
    pass

class MeaningRecordAdmin(RecordAdmin):
    pass

admin.site.register(Danci, DanciAdmin)
admin.site.register(WordmodeRecord, WordmodeRecordAdmin)
admin.site.register(MeaningmodeRecord, MeaningRecordAdmin)