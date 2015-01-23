from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.shortcuts import redirect

def create_organisation(form):
    form = form.cleaned_data
    username = form['org_name']
    email = form['email']
    first_name = form['first_name']
    last_name = form['last_name']
    password = form['password1']

    group = Group.objects.get(name='org')
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.groups.add(group)
    user.save()
    return user

def create_user(username, password, email):
    group = Group.objects.get(name='normal')
    user = User.objects.create_user(username=username, email=email, password=password)
    user.groups.add(group)
    user.save()
    return user

def user_to_login(username, password, email):
    user = authenticate(username=username, password=password)
    if user is None:
        try:
            user_object = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        username = user_object.username
        user = authenticate(username=username, password=d['password'])
    if user is not None:
        if user.is_active:
            return user
        else:
            return None
    else:
        return None

def group_redirect(user):
    if user.groups.filter(name='normal').exists():
        return redirect('player.views.player')
    elif user.groups.filter(name='org').exists():
        return redirect('org.views.awaiting')
    elif user.groups.filter(name='moderator').exists():
        return redirect('moderation.views.home')
    else:
        raise redirect('reg.views.index')