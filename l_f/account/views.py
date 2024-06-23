from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import views as auth_views

from .forms import ProfileEditForm

from .models import Profile
import time


@login_required
def dashboard(request):

    print(__name__)
    
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


@login_required
def change_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Profile.objects.filter(user=request.user).update(**cd)
            messages.success(request, 'Profile updated successfully')
            
            return render(request, 'account/dashboard.html', {'section': 'dashboard'})
        else:
            # если форма ошибка по бд или неправильные символы ввывести ошибку
            
            messages.error(request, form.errors)
            cd = form.cleaned_data
            print(form.errors)

            Profile.objects.filter(user=request.user).update(**cd)
            return render(request, 'account/dashboard.html', {'section': 'dashboard'})
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)

        return render(request, 'account/change_profile.html', {'form': profile_form})


def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создать новый объект пользователя,
            # но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Сохранить объект User
            new_user.save()

            # Создать профиль пользователя
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})
