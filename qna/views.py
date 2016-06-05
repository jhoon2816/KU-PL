from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Question

def question_list(request):
    questions = Question.objects.filter(created_date__lte = timezone.now()).order_by('-updated_date')
    return render(request, 'qna/question_list.htm', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'qna/question_detail.htm', {'question': question})
