from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Question

admin.site.register(Question)
