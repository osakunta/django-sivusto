from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    messages.add_message(request, messages.INFO, 'Hello world.')
    username = password = ''

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'The account is disabled.')

        else:
            messages.error(request, 'Wrong username or password.')

    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_user(request):
    logout(request)

    return HttpResponseRedirect('/')
