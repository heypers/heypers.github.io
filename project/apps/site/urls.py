from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home_redirect'),
    path('home/', views.index, name='index'),
    path('rules/', views.rules, name="rules"),
    path('login/', views.login, name='login'),
    path('oauth2/login/redirect/', views.oauth2_login_redirect,
         name='oauth2_login_redirect'),
    path("privacy/", views.privacy, name="privacy"),
    path("hrl/", views.hrl, name="hrl"),
    path("err/", views.error, name="error"),
    path("license/", views.license, name="license"),
    path("policy/", views.policy, name="policy")
]