from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .form import *


def index(request):
    return HttpResponse("hello world")


def admin(request):
    return render(request, "polls/admin/admin.html", )


def add_question(request):
    if request.method == "POST":
        question = Question(question=request.POST.get("question"))
        question.save()

        answers = request.POST.getlist("answer[]")
        for i in range(len(answers)):
            answer = Answer(answer=answers[i])
            questions_answers = QuestionsAnswers(question_id=question.id,
                                                 answer_id=answer.id,
                                                 correct=request.POST.get("correct[" + str(i) + "]") == "on")
            print(request.POST.get("correct[" + str(i) + "]"))
            answer.save()
            questions_answers.save()
        return redirect("admin")

    return render(request, "polls/admin/addQuestion.html", locals())


from .QuestionWrapper import QuestionWrapper


def edit_question(request):
    question_wrappers = get_questions()
    return render(request, "polls/admin/editQuestions.html", locals())


def get_statistic(request):
    question_statistics = dict()
    for s in Statistics.objects.all():
        question_statistics[s.question.question] = (s.right_answered_time / s.answered_time) * 100
    return render(request, "polls/admin/getStatistics.html", locals())


def client(request):
    question_wrappers = []
    if request.method == "GET":
        print(request.GET)
        print(request.GET.get('userName'))
        question_wrappers = get_questions()

    return render(request, "polls/client/client.html", locals())


def answer(request):
    question_wrappers = get_questions()
    result = 0
    if request.method == "POST":
        client_correct_answer = 0
        for qw in question_wrappers:
            client_answers = request.POST.getlist(str(qw.question.id))
            correct_answers = []
            updated_statistics = Statistics.objects.get(question_id=qw.question.id)

            updated_statistics.answered_time = updated_statistics.answered_time + 1

            for key in qw.answers.keys():
                if qw.answers[key]:
                    correct_answers.append(str(key.id))
            if correct_answers == client_answers:
                client_correct_answer = client_correct_answer + 1
                updated_statistics.right_answered_time = \
                    updated_statistics.right_answered_time + 1
            updated_statistics.save()
        result = (client_correct_answer * 100) / len(question_wrappers)

    return render(request, "polls/client/result.html", locals())


def get_questions():
    question_wrappers = []
    for q in Question.objects.all():
        questions_answers = QuestionsAnswers.objects.filter(question_id=q.id)
        answers = {}
        for qa in questions_answers:
            answers[Answer.objects.get(id=qa.answer_id)] = qa.correct
        question_wrappers.append(QuestionWrapper(q, answers))
    return question_wrappers


'''
import random


def get_random_questions():
    question_wrappers = []
    all_questions = Question.objects.all()

    for i in range(len(all_questions)):
        questions_answers = QuestionsAnswers.objects.filter(question_id=all_questions[i].id)
        answers = {}
        for qa in questions_answers:
            answer = Answer.objects.get(id=qa.answer_id)
            answers[answer] = qa.correct
        question_wrappers.append(QuestionWrapper(all_questions[i], answers))
    return question_wrappers
'''
