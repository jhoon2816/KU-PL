from django import forms
from django_summernote.widgets import SummernoteWidget
from django_summernote.widgets import SummernoteInplaceWidget
from .models import Question
from .models import Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'title',
            'content',
        )
        widgets = {
            'content': SummernoteInplaceWidget(),
            # 'content': SummernoteWidget(),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
            'content',
        )
        widgets = {
            'content': SummernoteInplaceWidget(),
            # 'content': SummernoteWidget(),
        }

# class ContentForm(forms.Form):
    # content = forms.CharField(widget=SummernoteInplaceWidget())
    # content = forms.CharField(widget=SummernoteWidget())
