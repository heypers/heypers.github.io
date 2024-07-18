
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.conf import settings
from django.contrib.sessions.models import Session

from core import Config

def home_redirect(request):
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def rules(request):
    return render(request, "rules.html")

def privacy(request):
    return render(request, "privacy.html")

def policy(request):
    return render(request, "policy.html")

def hrl(request):
    return render(request, "hrl.html")

def error(request):
    return render(request, "error.html")

def license(request):
    return redirect("http://www.apache.org/licenses/LICENSE-2.0")

def login(request):
    return redirect(Config.URL)

def oauth2_login_redirect(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponseBadRequest('Missing code')

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': Config.DISCORD_REDIRECT_URI,
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post('%s/oauth2/token' % Config.API_ENDPOINT, data=data, headers=headers,
                             auth=(Config.DISCORD_CLIENT_ID, Config.DISCORD_CLIENT_SECRET))
    if response.status_code != 200:
        print('Error fetching token:', response.text)
        return HttpResponseBadRequest(response.status_code, response.text)

    tokens = response.json()
    access_token = tokens['access_token']
    request.session['access_token'] = access_token
    request.session.permanent = True

    user_info_response = requests.get('%s/users/@me' % Config.API_ENDPOINT, headers={
        'Authorization': f'Bearer {access_token}'
    })
    if user_info_response.status_code != 200:
        print('Error fetching user info:', user_info_response.text)
        return HttpResponseBadRequest(user_info_response.status_code, user_info_response.text)

    user_info = user_info_response.json()
    request.session['user'] = {
        'id': user_info['id'],
        'username': user_info['username'],
        'discriminator': user_info['discriminator'],
        'avatar': user_info['avatar'],
        'email': user_info.get('email')
    }

    return redirect('dashboard')
