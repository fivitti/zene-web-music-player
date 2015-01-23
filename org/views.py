# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from models import Application
from forms import ApplicationForm
from iom.helpers import group_required
from org.helpers import create_application, generate_dict

# Create your views here.
@login_required
@group_required('org')
def new_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            create_application(form, request.user)
            return redirect('org.views.awaiting')
    else:
        form = ApplicationForm()
    return render(request, 'org/new_app.html', {'form': form})

@login_required
@group_required('org')
def awaiting(request):
    current_user = request.user
    d = generate_dict('a', current_user)
    return render(request, 'org/awaiting.html', d)

@login_required
@group_required('org')
def settled(request):
    current_user = request.user
    d = generate_dict('s', current_user)
    return render(request, 'org/awaiting.html', d)

@login_required
@group_required('org')
def detail(request, app_id):
    app = get_object_or_404(Application, id=app_id)
    red = [('Powód', app.title),
           ('Zgłoszony', app.user.username),
           ('Opis', app.description),
           ('Status', 'Oczekuje na rozpatrzenie' if app.status == 'a' else 'Rozpatrzone'),
           ('Odpowiedź' if app.answer else '', app.answer),
           ]
    return render(request, 'org/detail.html', {'red': red, 'date': app.date_create})