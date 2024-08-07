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

from django.urls import path
from . import views
from django.urls import path
from .views import BaseModelListView, BaseModelDetailView, BaseModelCreateView, BaseModelUpdateView, BaseModelDeleteView

urlpatterns = [
    path('', views.home_redirect, name='home_redirect'),
    path('home/', views.index, name='index'),
    path('rules/', views.rules, name="rules"),
    path('accounts/login/', views.login, name='login'),
    path('oauth2/login/redirect/', views.oauth2_login_redirect,
         name='oauth2_login_redirect'),
    path("privacy/", views.privacy, name="privacy"),
    path("hrl/", views.hrl, name="hrl"),
    path('err/<str:message>/', views.error, name='error'),
    path("license/", views.license, name="license"),
    path("policy/", views.policy, name="policy"),

    path('<str:model>/create/', BaseModelCreateView.as_view(), name='base_model_create'),
    path('<str:model>/<int:pk>/edit/', BaseModelUpdateView.as_view(), name='base_model_update'),
    path('<str:model>/', BaseModelListView.as_view(), name='base_model_list'),
    path('<str:model>/<int:pk>/', BaseModelDetailView.as_view(), name='base_model_detail'),
    path('<str:model>/<int:pk>/delete/', BaseModelDeleteView.as_view(), name='base_model_delete'),
]
