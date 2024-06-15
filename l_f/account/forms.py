from typing import Any
from django import forms
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
<<<<<<< HEAD
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import PasswordChangeForm
=======
from django.contrib.auth.models import User
>>>>>>> c8716cc135391a253c88b23743226fe6076458fd
>>>>>>> 6f0f0587a916ca3ecf309a132c18cca079c5f0a9


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


<<<<<<< HEAD
=======
<<<<<<< HEAD
class ChangePasswordForm_ru(PasswordChangeForm):
    pass

=======
>>>>>>> 6f0f0587a916ca3ecf309a132c18cca079c5f0a9
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
<<<<<<< HEAD
=======
>>>>>>> c8716cc135391a253c88b23743226fe6076458fd
>>>>>>> 6f0f0587a916ca3ecf309a132c18cca079c5f0a9
