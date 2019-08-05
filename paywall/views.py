import django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Secret

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    user = django.contrib.auth.authenticate(
        request,
        username=request.POST.get('username'), 
        password=request.POST.get('password')
    ) 
    if not user:
        return redirect('/')

    django.contrib.auth.login(request, user)

    return redirect('/paywall')

@login_required
def paywalled(request):
    secret = Secret(code="1234")
    return render(request, 'paywalled.html', {"code": secret.code})

@login_required
def paywalled_ajax(request):
    secret = Secret(code="5678")
    return JsonResponse({'code': secret.code})
