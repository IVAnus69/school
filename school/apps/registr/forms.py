from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):  # Форма регистрации
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(forms.Form):  # Форма авторизации
    username = forms.CharField(label='Имя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class ChangeUserProfileForm(forms.Form):
    username = forms.CharField(label='Имя', widget=forms.TextInput())
    email = forms.EmailField(label='Почта', widget=forms.TextInput())
    image = forms.ImageField(label='Обновить изображение профиля', required=False)
    password = forms.CharField(label='Новый пароль', required=False)