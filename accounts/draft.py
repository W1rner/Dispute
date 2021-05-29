def generate_code():
    random.seed()
    return str(random.randint(10000,99999))

def register(request):
    if not request.user.is_authenticated:
        if request.POST:
            signupform = SignUpForm(request.POST)
            if signupform.is_valid():
                signupform.save()
                username = signupform.cleaned_data.get('username')
                email = signupform.cleaned_data.get('email')
                password1 = signupform.cleaned_data.get('password')
                # user = User.objects.create_user(username=signupform.data['username'], email=signupform.data['email'], password=signupform.data['password'])
                user_f = User.objects.get(username=username, email=email, is_active=False)
                # if IntegrityError:
                #     messages.add_message(request, messages.ERROR, "Пользователь уже существует")
                #     return redirect('/account/signup/')
                code = generate_code()
                if Profile.objects.filter(code=code):
                    code = generate_code()

                message = code
                user = authenticate(username=username, password=password1)
                now = datetime.datetime.now()

                Profile.objects.create(user=user_f, code=code, date=now)

                send_mail(
                    'Код подтверждения.',
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False
                )
                if user and user.is_active:
                    login(request, user)
                    return redirect('/account/user/')
                else: #тут добавить редирект на страницу с формой для ввода кода.
                    form.add_error(None, 'Аккаунт не активирован')
                    return redirect('/account/activation_code_form/')
                    # return render(request, 'registration/register.html', {'form': form})

            else:
                return render(request, 'signup.html', {'form': form})
        else:
            return render(request, 'signup.html', {'form': SignUpForm()})
    else:
        return redirect('/account/user/')

def endreg(request):
    if  request.user.is_authenticated:
        return redirect('/account/user/')
    else:
        if request.method == 'POST':
            form = MyActivationCodeForm(request.POST)
            if form.is_valid():
                code_use = form.cleaned_data.get("code")
                if Profile.objects.filter(code=code_use):
                    profile = Profile.objects.get(code=code_use)
                else:
                    form.add_error(None, "Код подтверждения не совпадает.")
                    return render(request, 'activation_code_form.html', {'form': form})
                if profile.user.is_active == False:
                    profile.user.is_active = True
                    profile.user.save()
                    # user = authenticate(username=profile.user.username, password=profile.user.password)
                    login(request, profile.user)
                    profile.delete()
                    return redirect('/account/user/')
                else:
                    form.add_error(None, '1 Unknown or disabled account')
                    return render(request, 'activation_code_form.html', {'form': form})
            else:
                return render(request, 'activation_code_form.html', {'form': form})
        else:
            form = MyActivationCodeForm()
            return render(request, 'activation_code_form.html', {'form': form})











    ____________________________
    def SignUpView(request):
        if request.method == 'POST':
            signupform = SignUpForm(request.POST)
            if signupform.is_valid():
                try:
                    user = User.objects.create_user(username=signupform.data['username'], email=signupform.data['email'], password=signupform.data['password'])
                except IntegrityError:
                    messages.add_message(request, messages.ERROR, "Пользователь уже существует")
                    return redirect('/account/signup/')
                user.save()
                login(request, user)
                return redirect('/account/user/')
            else:
                messages.add_message(request, messages.ERROR, "Некорректные данные в форме")
        else:
            pass

        context = {}
        context['signupform'] = SignUpForm()

        return render(request, 'signup.html', context)






___________________________________________________





if not request.user.is_authenticated:
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.create_user(username=form.data['username'], email=form.data['email'], password=form.data['password'])
            # user_f = User.objects.get(username=username, email=email, is_active=False)
            # if IntegrityError:
            #     messages.add_message(request, messages.ERROR, "Пользователь уже существует")
            #     return redirect('/account/signup/')
            code = generate_code()
            if Profile.objects.filter(code=code):
                code = generate_code()

            message = code
            # user = authenticate(username=username, password=password1)
            now = datetime.datetime.now()

            Profile.objects.create(user=user, code=code, date=now)

            send_mail(
                'Код подтверждения.',
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            if user and user.is_active:
                login(request, user)
                return redirect('/account/user/')
            else: #тут добавить редирект на страницу с формой для ввода кода.
                form.add_error(None, 'Аккаунт не активирован')
                return redirect('/account/activation_code_form/')
                # return render(request, 'registration/register.html', {'form': form})

        else:
            return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'signup.html', {'form': SignUpForm()})
else:
    return redirect('/account/user/')

def EndSignUpView(request):
if  request.user.is_authenticated:
    return redirect('/account/user/')
else:
    if request.method == 'POST':
        form = MyActivationCodeForm(request.POST)
        if form.is_valid():
            code_use = form.cleaned_data.get("code")
            if Profile.objects.filter(code=code_use):
                profile = Profile.objects.get(code=code_use)
            else:
                form.add_error(None, "Код подтверждения не совпадает.")
                return render(request, 'activation_code_form.html', {'form': form})
            if profile.user.is_active == False:
                profile.user.is_active = True
                profile.user.save()
                # user = authenticate(username=profile.user.username, password=profile.user.password)
                login(request, profile.user)
                profile.delete()
                return redirect('/account/user/')
            else:
                form.add_error(None, '1 Unknown or disabled account')
                return render(request, 'activation_code_form.html', {'form': form})
        else:
            return render(request, 'activation_code_form.html', {'form': form})
    else:
        form = MyActivationCodeForm()
        return render(request, 'activation_code_form.html', {'form': form})
