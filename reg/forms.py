# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from helpers import user_to_login

class OrganisationForm(forms.Form):
    org_name = forms.CharField(label='Nazwa organizacji')
    email = forms.EmailField(label='E-mail:')
    first_name = forms.CharField(label='Imie')
    last_name = forms.CharField(label='Nazwisko')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')

    def clean(self):
        cleaned_data = super(OrganisationForm, self).clean()
        self.clean_password(cleaned_data)
        self.clean_email_my(cleaned_data)
        self.clean_username_my(cleaned_data)

    def clean_password(self, cleaned_data):
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            msg = "Hasła muszą być identyczne."
            self.add_error('password1', msg)
            #raise forms.ValidationError(msg)

    def clean_email_my(self, cleaned_data):
        email = cleaned_data.get('email')
        if User.objects.filter(email=email):
            msg = "E-mail jest zajęty"
            self.add_error('email', msg)

    def clean_username_my(self, cleaned_data):
        username = cleaned_data.get('org_name')
        if User.objects.filter(username=username):
            msg = "Taka organizacja już istnieje w systemie."
            self.add_error('org_name', msg)

class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika lub e-mail')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        email = cleaned_data.get('email')
        user = user_to_login(username, password, email)
        if user is None:
            raise forms.ValidationError('Użytkownik nie istnieje lub błędne hasło.')

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        self.clean_password(cleaned_data)
        self.clean_email_my(cleaned_data)
        self.clean_username_my(cleaned_data)

    def clean_password(self, cleaned_data):
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            msg = "Hasła muszą być identyczne."
            self.add_error('password1', msg)
            #raise forms.ValidationError(msg)

    def clean_email_my(self, cleaned_data):
        email = cleaned_data.get('email')
        if User.objects.filter(email=email):
            msg = "E-mail jest zajęty"
            self.add_error('email', msg)

    def clean_username_my(self, cleaned_data):
        username = cleaned_data.get('username')
        if User.objects.filter(username=username):
            msg = "Taki użytkownik już istnieje w systemie."
            self.add_error('username', msg)
