from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def redirect_to_discord(request):
    return HttpResponseRedirect('https://discord.gg/k8AMSqDfCW')