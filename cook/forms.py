from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    '''Авторизация пользователя'''
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    '''Регистрация пользователя'''
    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self, commit=True):
        '''Шифрование пароля, помещаем его в БД. Для сохранения пользователя'''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
