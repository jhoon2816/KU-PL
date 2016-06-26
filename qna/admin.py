from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Question
from .models import Answer

class QuestionAdmin(SummernoteModelAdmin):
    class Meta:
        model = Question
        fields = (
            'title',
            'content',
        )

class AnswerAdmin(SummernoteModelAdmin):
    class Meta:
        model = Question
        fields = (
            'content',
        )

admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer, AnswerAdmin)
