# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import login
from forms import OrganisationForm, LoginForm, RegisterForm
from helpers import create_organisation, user_to_login, create_user, group_redirect

# Create your views here.
def org(request):
    if request.method == 'POST':
        form = OrganisationForm(request.POST)
        if form.is_valid():
            organisation = create_organisation(form)
            organisation.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, organisation)
            return redirect('org.views.awaiting')
    else:
        form = OrganisationForm()
    return render(request, 'reg/org.html', {'form': form})

def index(request):
    if request.user.is_authenticated() and not request.user.is_staff:
        return group_redirect(request.user)
    login_form = LoginForm()
    register_form = RegisterForm()
    return render(request, 'reg/index.html', {'login_form': login_form, 'register_form': register_form})

def login_my(request):
    if 'login' in request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            form = login_form.cleaned_data
            username = form.get('username')
            password = form.get('password')
            email = form.get('email')
            user = user_to_login(username, password, email)
            login(request, user)
            return group_redirect(user)
    else:
        login_form = LoginForm()
    register_form = RegisterForm()

    return render(request, 'reg/index.html', {'login_form': login_form, 'register_form': register_form})

def register_my(request):
    if 'register' in request.POST:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            form = register_form.cleaned_data
            username = form.get('username')
            password = form.get('password1')
            email = form.get('email')
            new_user = create_user(username, password, email)
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)
            return redirect('player.views.player')
    else:
        register_form = RegisterForm()
    login_form = LoginForm()

    return render(request, 'reg/index.html', {'login_form': login_form, 'register_form': register_form})