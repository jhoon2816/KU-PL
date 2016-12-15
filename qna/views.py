from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .forms import QuestionForm
from .forms import AnswerForm
from .models import Question
from .models import Answer

def question_list(request):
    questions = Question.objects.filter(created_date__lte = timezone.now()).order_by('-updated_date')
    return render(request, 'qna/question_list.htm', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.updated_date = timezone.now()
            answer.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = AnswerForm()

    return render(request, 'qna/question_detail.htm', {'question': question, 'form': form})

def question_new(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        # View 가 Controller 역할을 한다.
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.updated_date = timezone.now()
            question.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'qna/question_edit.htm', {'form': form})

def question_edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.updated_date = timezone.now()
            question.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'qna/question_edit.htm', {'form': form})

def question_remove(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('question_list')

