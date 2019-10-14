from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Chapter, Binding

class ChapterAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Binding) 