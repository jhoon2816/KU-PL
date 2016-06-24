from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Question
from .models import Answer

admin.site.register(Question)
admin.site.register(Answer)
