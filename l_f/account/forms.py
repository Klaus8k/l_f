from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import PasswordChangeForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ChangePasswordForm_ru(PasswordChangeForm):
    pass

