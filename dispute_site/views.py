from django.shortcuts import render, redirect
from time import time, ctime

from dispute_site.models import Commentary
from django.contrib.auth.models import User
from django.template import RequestContext

from django.db import IntegrityError

from dispute_site.forms import *



def making_questions_dictlist(filter=time()):
    questions = Question.objects.all()
    questions_dictlist = []

    for quest in questions:
        if quest.time >= (time() - filter):
            questions_dictlist.append({
                'id': quest.id,
                'header': quest.header,
                'text': quest.text,
                'category': quest.category,
                'user': quest.user,
                'rating': quest.rating,
                'time': ctime(quest.time),
            })

    return questions_dictlist

def making_comments_dictlist():
    comments = Commentary.objects.all()
    comments_dictlist = []
    for comment in comments:
        comments_dictlist.append({
            'text': comment.text,
            'user': comment.user,
            'time': ctime(comment.time),
        })

    return comments_dictlist


# Create your views here.
def about_page(request):
    return render(request, 'about.html')


def error_page(request):
    return render(request, 'error.html')


def custom_404_page(request, exception):
    return render(request, '404.html')


def userpage_page(request):
    user_id = request.GET.get('id', None)

    if user_id is None:
        return redirect('/error/')

    try:
        current_user = User.objects.get(id=int(user_id))
    except User.DoesNotExist:
        return redirect('/error/')

    if current_user is not None:
        context = {
            'username': current_user.username,
            'user_id': int(user_id),
            'last_login': current_user.last_login,
        }
    else:
        return redirect('/error/')

    return render(request, 'userpage.html', context)


def popular_page(request):
    hour = 3600
    day = 86400
    month = 2419200 # месяц = 4 недели
    alltime = time()

    filter = month

    context = {
        'filter': filter,
        'questions': sorted(making_questions_dictlist(filter), key=lambda k: k['rating'], reverse=True),
    }

    return render(request, 'popular.html', context)


def cathegory_page(request):
    users = User.objects.all()
    users_dictlist = []

    for user in users:
        users_dictlist.append({
            'id': user.id,
            'username': user.username,
        })

    context = {
        'users': users_dictlist,
    }
    return render(request, 'cathegory.html', context)


def recomended_page(request):
    return render(request, 'recomended.html')


def create_question_page(request):
    context = {
            'form' : QuestionForm,
            }

    question_form = QuestionForm(request.POST)

    if request.method == 'POST':
        if question_form.is_valid() and request.user.is_authenticated:
            question = Question(header=question_form.cleaned_data['header'],
                                text=question_form.cleaned_data['text'],
                                user=request.user)
            question.save()
            return redirect('/questions/')
    return render(request, 'create_question.html', context)


def quest_page(request):
    quest_id = request.GET.get('id', None)

    if quest_id is None:
        return redirect('/error/')
    try:
        current_quest = Question.objects.get(id=int(quest_id))
    except Question.DoesNotExist:
        return redirect('/error/')

    current_quest = Question.objects.get(id=int(quest_id))

    if current_quest is not None:
        context = {
            'question' : current_quest,
            'quest_id': int(quest_id),
            # 'header': current_quest.header,
            # 'text': current_quest.text,
            # 'user': current_quest.user,
            # 'category': current_quest.category,
            'time': ctime(current_quest.time),
            # 'rating': current_quest.rating,
            'commentform' : CommentaryForm,
            'comments' : making_comments_dictlist()
        }
    else:
        return redirect('/error/')

    # if not request.user.is_authenticated:
    #     return redirect('/account/login/')

    comment_form = CommentaryForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid() and request.user.is_authenticated:
            comment = Commentary(parent_id=int(quest_id),
                                text=comment_form.cleaned_data['text'],
                                user=request.user)
            comment.save()
            # return redirect('/')

    return render(request, 'commentary.html', context)


def questions_page(request):

    context = {
        'questions': making_questions_dictlist(),
    }

    return render(request, 'questions.html', context)
