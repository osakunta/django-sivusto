from django.http import *
from django.shortcuts import render
from django.contrib.auth import logout


def logout_user(request):
    logout(request)

    return HttpResponseRedirect('/')


def handler404(request, *args, **kwargs):
    return render(request, '404.html', status=404)


def handler500(request, *args, **kwargs):
    return render(request, '500.html', status=500)
