from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = (
            'title',
            'content',
        )
        widgets = {
            'content': SummernoteWidget(),
            # 'content': SummernoteInplaceWidget(),
        }

class ContentForm(forms.Form):
    content = forms.CharField(widget=SummernoteWidget())
    # content = forms.CharField(widget=SummernoteInplaceWidget())
