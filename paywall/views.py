import json
import django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.core import serializers

from .models import Secret
from .utils import validate_code

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

def secret(request):
    if request.method == 'GET':
        return secret_get(request)

    elif request.method == 'POST':
        return secret_post(request)

    elif request.method == 'PUT':
        return secret_put(request)

    elif request.method == 'DELETE':
        return secret_delete(request)

    else:
        return JsonResponse({'message': 'Invalid method'}, status=400)

def secret_get(request):
    return HttpResponse(serializers.serialize('json', Secret.objects.all()), content_type='application/json')

def secret_post(request):
    post_data = json.loads(request.body)
    code = post_data.get('code')

    # do some validation, how about must be length = 4, can't start with a zero, must be numeric
    valid, error = validate_code(code)

    if valid:
        Secret.objects.update_or_create(code=int(code))

        return JsonResponse({'message': 'Inserted new secret'})

    else:
        return JsonResponse({'error': f'Unable to create new secret. Error: {error}'}, status=400)

def secret_put(request):
    from_code = request.GET.get('from')
    to_code = request.GET.get('to')

    valid_from, error_from = validate_code(from_code)
    valid_to, error_to = validate_code(to_code)

    if valid_from and valid_to:
        secret = Secret.objects.get(code=int(from_code))
        secret.delete()
        secret.code = int(to_code)
        secret.save()

        return JsonResponse({'message': f'Changed secret {from_code} to {to_code}'})

    else:
        return JsonResponse({'error': f'Invalid code or codes. Errors: {error_from}, {error_to}'}, status=400)

def secret_delete(request):
    code = request.GET.get('code')

    valid, error = validate_code(code)

    if valid:
        try:
            Secret.objects.get(code=int(code)).delete()

        except Secret.DoesNotExist:
            return JsonResponse({'error': '{code} does not exist.'}, status=400)

        return JsonResponse({'message': f'Deleted secret {code}'})

    else:
        return JsonResponse({'error': f'Invalid code. Error: {error}'}, status=400)
