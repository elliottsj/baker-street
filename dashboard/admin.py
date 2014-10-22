from dashboard.models import Document, Question
from django.contrib import admin


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'document')
    list_filter = ['document']
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Document on which this question was asked', {'fields': ['document']})
    ]


class DocumentAdmin(admin.ModelAdmin):
    fields = ['title', 'publish_date']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Document, DocumentAdmin)
