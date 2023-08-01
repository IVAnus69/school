from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm, UserLoginForm, ChangeUserProfileForm
from .models import Profile, ExerciseReady


def profile(request):  # Страница профиля
    prof = Profile.objects.get(user=request.user)
    exercise_ready = ExerciseReady.objects.filter(profile_id=prof).order_by("exercise_id")
    image = prof.image

    def render_profile(form):
        return render(request, 'profile.html', {'form': form,
                                                'image': image,
                                                'exercise_ready': exercise_ready})

    if request.method == 'POST':
        if 'save_button' in request.POST:
            form = ChangeUserProfileForm(request.POST)
            if form.is_valid():
                if request.POST.get('image') != '':
                    file = request.FILES['image']
                    prof.image = file

                prof.user.username = request.POST.get('username')

                get_email = request.POST.get('email')
                get_user_email = User.objects.values_list('email', flat=True)
                if get_email != request.user.email:
                    if get_email not in get_user_email:
                        prof.user.email = request.POST.get('email')
                    else: form.add_error(None, 'Такая почта уже есть')

                get_password = request.POST.get("password")
                if get_password != '':
                    if get_password.strip() != '':
                        prof.user.set_password(request.POST.get("password"))
                    else: form.add_error(None, 'Вы ввели неверные знаки пароля')

                try:
                    prof.user.save()
                    prof.save()
                    login(request, prof.user)
                except Exception as e:
                    e = type(e).__name__
                    if e == 'IntegrityError':
                        form.add_error(None, f'Такой ник уже существует {e}')

                return render_profile(form)
            return HttpResponseRedirect("/")
    else:
        initial_dict = {
            'username': prof.user.username,
            'email': prof.user.email
        }
        form = ChangeUserProfileForm(initial=initial_dict)
        return render_profile(form)


def registration(request):  # Регистрация
    def update_user_data(user):  # Создать профиль по user
        Profile.objects.update_or_create(user=user)

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            update_user_data(user)
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            form.add_error(None, "Неверно введены данные (проверьте правильность введенного пароля)")
            return render(request, 'registration.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'registration.html', {'form': form})


def auth(request):  # Аутенфикация
    def render_auth(form):
        return render(request, 'login.html', {'form': form})

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            try:
                login(request, user)
            except AttributeError:
                form.add_error(None, "Неверный пароль")
                return render_auth(form)
            return HttpResponseRedirect('/')
        else:
            form.add_error(None, 'Неверно введены данные')
            return render_auth(form)
    else:
        form = UserLoginForm()
        return render_auth(form)


def close_auth(request):
    logout(request)
    return HttpResponseRedirect("/")


# todo логин и дописать регистрацию
# todo Кэш реализовать (разобраться с тем что запихать в кэш)
# todo Подписать существующие функции
