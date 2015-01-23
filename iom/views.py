from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('reg.views.index')

def index(request):
    return redirect('reg.views.index')
