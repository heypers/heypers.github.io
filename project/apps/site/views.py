"""
Copyright 2023 mr_fortuna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import requests
from core import InformationForm
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from core import Config
from . import login_required
from .models import Information


# from django.conf import settings
# from django.contrib.sessions.models import Session

@login_required
def information_list(request):
    informations = Information.objects.all()
    return render(request, 'information_list.html', {'informations': informations})


@login_required
def information_detail(request, pk):
    information = get_object_or_404(Information, pk=pk)
    return render(request, 'information_detail.html', {'information': information})


@login_required
def information_edit(request, pk):
    information = get_object_or_404(Information, pk=pk)
    if request.method == "POST":
        form = InformationForm(request.POST, instance=information)
        if form.is_valid():
            information = form.save(commit=True)
            return redirect('information_detail', pk=information.pk)
    else:
        form = InformationForm(instance=information)
    return render(request, 'information_edit.html', {'form': form})


@login_required
def information_create(request):
    if request.method == "POST":
        form = InformationForm(request.POST)
        if form.is_valid():
            information = form.save(commit=True)
            return redirect('information_detail', pk=information.pk)
    else:
        form = InformationForm()
    return render(request, 'information_create.html', {'form': form})


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
    user_id = user_info['id']
    request.session['user'] = {
        'id': user_id,
        'username': user_info['username'],
        'discriminator': user_info['discriminator'],
        'avatar': user_info['avatar'],
        'email': user_info.get('email')
    }

    if user_id not in Config.ALLOWED_USER_IDS:
        return render(request, 'error.html', {'message': 'Unauthorized user'})

    return redirect('hrl')


@login_required
def hrl(request):
    return render(request, "hrl.html")


def login(request):
    return redirect(Config.URL)


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


def error(request, message):
    return render(request, 'error.html', {'message': message})


def license(request):
    return redirect("http://www.apache.org/licenses/LICENSE-2.0")
