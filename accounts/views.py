from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from random import randint

from .forms import SignUpForm, LoginForm, ProfileEditForm


def user_page(request):
    return render(request, 'user.html')

def premium_page(request):
    return render(request, 'premium.html')

def userpage_page(request):
    return render(request, 'userpage.html')

def LoginView(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user = authenticate(request, username=loginform.data['username'], password=loginform.data['password'])

            if user != None:
                login(request, user)
                return redirect('/account/')
            else:
                messages.add_message(request, messages.ERROR, "Неправильное имя пользователя или пароль")
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме")
    else:
        pass

    context = {}
    context['loginform'] = LoginForm()
    return render(request, 'login.html', context)

def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            if form.data['password1'] == 'qq':
                try:
                    user = User.objects.create_user(username=form.data['username'], email=form.data['email'], password=form.data['password1'])
                except IntegrityError:
                    messages.add_message(request, messages.ERROR, "Пользователь c таким именем уже существует")
                    return redirect('/account/signup/')

            elif form.data['password1'] != form.data['password2']:
                messages.add_message(request, messages.ERROR, "Пароли не совпадают")
                return redirect('/account/signup/')
            elif len(form.data['password1']) < 8:
                messages.add_message(request, messages.ERROR, "Пароль должен содержать не менее восьми символов")
                return redirect('/account/signup/')
            elif form.data['password1'].isnumeric():
                messages.add_message(request, messages.ERROR, "Пароль должен содержать не только цифры")
                return redirect('/account/signup/')
            else:
                try:
                    user = User.objects.create_user(username=form.data['username'], email=form.data['email'], password=form.data['password1'])
                except IntegrityError:
                    messages.add_message(request, messages.ERROR, "Пользователь c таким именем уже существует")
                    return redirect('/account/signup/')

            user.save()
            login(request, user)
            return redirect('/account')
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме")
    else:
        pass

    context = {}
    context['form'] = SignUpForm()

    return render(request, 'signup.html', context)


def user_edit_profile_page(request):
    context = {}

    if request.user.is_authenticated:
        context['username'] = request.user.username.title()
        # context['firstname'] = request.user.first_name
        # context['lastname'] = request.user.last_name
        # context['age'] = request.user.age
        # context['mental_age'] = request.user.mental_age
        context['email'] = request.user.email
        context['userlogin'] = request.user.username
        context['user_logged_in'] = True
    else:
        return redirect('/login/')


    if request.user.is_authenticated:
        form = ProfileEditForm(request.POST)
        context['form'] = form
        if request.method == 'POST':
            print(request.user)
            if form.is_valid():

                if form.data['username'] != '':
                    request.user.username = form.data['username']

                if form.data['email'] != '':

                    request.user.email = form.data['email']

                if form.data['oldpassword'] != '' and authenticate(request,
                        username=request.user.username,
                        password=form.data['oldpassword'] ) != None :
                    print("================")
                    print("PASSWORD CORRECT")
                    print("================")
                    print(form.data.get('password1'))
                    if form.data.get('password1') == form.data.get('password2') and \
                            form.data.get('password1') != None:
                                print("SETTING NEW PASSWORDS")
                                print(form.data.get('password1'))
                                request.user.set_password(form.data.get('password1'))
                                cp_user = authenticate(username=request.user.username, password=form.data.get('password2'))
                                login(request, cp_user)
                request.user.save()



        # str(firstname) != "" and firstname != None or str(lastname) != "" and lastname != None or \
        #if not any(user.username == userlogin for user in User.objects.all()):
        #    return redirect('')

    return render(request, 'edit_profile.html', context)
