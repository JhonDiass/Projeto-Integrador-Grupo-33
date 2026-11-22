# produtos/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def pre_login(request):
    return render(request, 'pre_login.html')

@login_required
def home(request):
    return render(request, 'home.html')