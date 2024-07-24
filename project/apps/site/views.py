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
from django.http import HttpResponseBadRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from core import Config
from .model_map import MODEL_MAP
from . import login_required, permission_check
from core.app.forms import InformationForm, CharacterForm, ObjectForm, ProtocolForm, LocationForm, LoreForm, PlotForm, DepartmentForm, DocumentForm, OrganizationForm, GroupForm, TechnologyForm
from .mixins import LoginRequiredMixin, PermissionRequiredMixin


def get_model_verbose_name(model_name):
    model = MODEL_MAP.get(model_name)
    if model is None:
        raise Http404(f"Model '{model_name}' not found.")
    return model._meta.verbose_name, model._meta.verbose_name_plural


class BaseModelListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'base_model_list.html'
    required_permission = 'scenarist'

    def get_queryset(self):
        model_name = self.kwargs['model']
        model = MODEL_MAP.get(model_name)
        if model is None:
            raise Http404(f"Model '{model_name}' not found.")
        return model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs['model']
        model = MODEL_MAP.get(model_name)
        context['model_verbose_name_plural'] = model._meta.verbose_name_plural
        context['model_name'] = model_name
        return context


class BaseModelDetailView(LoginRequiredMixin, DetailView):
    template_name = 'base_model_detail.html'

    def get_object(self):
        model_name = self.kwargs['model']
        model = MODEL_MAP.get(model_name)
        if model is None:
            raise Http404(f"Model '{model_name}' not found.")
        pk = self.kwargs['pk']
        return get_object_or_404(model, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs['model']
        verbose_name, verbose_name_plural = get_model_verbose_name(model_name)
        context['model_name'] = model_name
        context['verbose_name'] = verbose_name
        context['verbose_name_plural'] = verbose_name_plural
        return context


class BaseModelCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'base_model_form.html'
    required_permission = 'scenarist'

    def get_form_class(self):
        model_name = self.kwargs['model']
        form_classes = {
            'information': InformationForm,
            'lore': LoreForm,
            'plot': PlotForm,
            'location': LocationForm,
            'department': DepartmentForm,
            'organization': OrganizationForm,
            'object': ObjectForm,
            'protocol': ProtocolForm,
            'character': CharacterForm,
            'group': GroupForm,
            'technology': TechnologyForm,
            'document': DocumentForm
        }
        if model_name in form_classes:
            return form_classes[model_name]
        raise Http404(f"Model '{model_name}' not found.")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        model_name = self.kwargs['model']
        model = MODEL_MAP.get(model_name)
        if model is None:
            raise Http404(f"Model '{model_name}' not found.")
        self.object.__class__ = model
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        model_name = self.kwargs['model']
        return reverse('base_model_detail', kwargs={'model': model_name, 'pk': self.object.pk})


class BaseModelUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'base_model_form.html'
    required_permission = 'scenarist'

    def get_form_class(self):
        model_name = self.kwargs['model']
        form_classes = {
            'information': InformationForm,
            'lore': LoreForm,
            'plot': PlotForm,
            'location': LocationForm,
            'department': DepartmentForm,
            'organization': OrganizationForm,
            'object': ObjectForm,
            'protocol': ProtocolForm,
            'character': CharacterForm,
            'group': GroupForm,
            'technology': TechnologyForm,
            'document': DocumentForm
        }
        if model_name in form_classes:
            return form_classes[model_name]
        raise Http404(f"Model '{model_name}' not found.")

    def get_object(self):
        model_name = self.kwargs['model']
        model = MODEL_MAP.get(model_name)
        if model is None:
            raise Http404(f"Model '{model_name}' not found.")
        pk = self.kwargs['pk']
        return get_object_or_404(model, pk=pk)

    def get_success_url(self):
        model_name = self.kwargs['model']
        return reverse_lazy('base_model_detail', kwargs={'model': model_name, 'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs['model']
        verbose_name, verbose_name_plural = get_model_verbose_name(model_name)
        context['model_name'] = model_name
        context['verbose_name'] = verbose_name
        context['verbose_name_plural'] = verbose_name_plural
        return context


class BaseModelDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    required_permission = 'scenarist'
    template_name = 'base_model_confirm_delete.html'

    def get_object(self):
        model_name = self.kwargs['model']
        model = MODEL_MAP.get(model_name)
        if model is None:
            raise Http404(f"Model '{model_name}' not found.")
        pk = self.kwargs['pk']
        return get_object_or_404(model, pk=pk)

    def get_success_url(self):
        model_name = self.kwargs['model']
        return reverse_lazy('base_model_list', kwargs={'model': model_name})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs['model']
        verbose_name, verbose_name_plural = get_model_verbose_name(model_name)
        context['model_name'] = model_name
        context['verbose_name'] = verbose_name
        context['verbose_name_plural'] = verbose_name_plural
        return context


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

    if user_id not in Config.SCENARIST_IDS:
        return render(request, 'error.html', {'message': 'Unauthorized user'})

    return redirect('hrl')


@login_required
@permission_check('scenarist')
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
