from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import inlineformset_factory
from django.db import transaction
from .models import Exam, Question, Choice
from .forms import ExamForm, QuestionForm, ChoiceFormSet


def exam_list(request):
    """View to list all exams"""
    exams = Exam.objects.all().order_by('-created_date')
    return render(request, 'quiz/exam_list.html', {'exams': exams})


def exam_detail(request, exam_id):
    """View to display the details of a specific exam"""
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all().prefetch_related('choices')
    return render(request, 'quiz/exam_detail.html', {'exam': exam, 'questions': questions})


def exam_create(request):
    """View to create a new exam"""
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(request, 'Examen creado correctamente.')
            return redirect('question_create', exam_id=exam.id)
    else:
        form = ExamForm()

    return render(request, 'quiz/exam_form.html', {'form': form})


def question_create(request, exam_id):
    """View to create a new question"""
    exam = get_object_or_404(Exam, id=exam_id)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)

        if question_form.is_valid():
            with transaction.atomic():
                # Save the question
                question = question_form.save(commit=False)
                question.exam = exam
                question.save()

                # Proceses the choices
                formset = ChoiceFormSet(request.POST, instance=question)
                if formset.is_valid():
                    formset.save()

                    # Check if there is exactly one correct answer
                    correct_count = question.choices.filter(
                        is_correct=True).count()
                    if correct_count != 1:
                        messages.warning(
                            request, 'Debe haber exactamente una respuesta correcta.')
                    else:
                        messages.success(
                            request, 'Pregunta añadida correctamente.')

                    # Choice to redirect
                    if 'add_another' in request.POST:
                        return redirect('question_create', exam_id=exam.id)
                    else:
                        return redirect('exam_detail', exam_id=exam.id)
    else:
        question_form = QuestionForm()
        formset = ChoiceFormSet()

    return render(request, 'quiz/question_form.html', {
        'exam': exam,
        'question_form': question_form,
        'formset': formset,
    })
