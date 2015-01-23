# -*- coding: utf-8 -*-
__author__ = 'HP'
from django import forms
from django.contrib.auth.models import User

class ApplicationForm(forms.Form):
    title = forms.CharField(max_length=255, label='Powód zgłoszenia')
    user = forms.CharField(label='Użytkownik zgłaszany')
    description = forms.CharField(label='Opis', widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))

    def clean(self):
        cleaned_data = super(ApplicationForm, self).clean()
        self.clean_username_my(cleaned_data)

    def clean_username_my(self, cleaned_data):
        user = cleaned_data.get('user')
        user_exist = User.objects.filter(username=user)
        if not user_exist:
            msg = "Nie istnieje taki użytkownik."
            self.add_error('user', msg)
        user = User.objects.get(username=user)
        if not user.groups.filter(name='normal').exists():
            msg = "Podany użytkownik nie może zostać zgłoszony."
            self.add_error('user', msg)