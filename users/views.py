from django.shortcuts import render
from django.contrib.auth import authenticate, login as dj_login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.core.mail import send_mail, BadHeaderError


def register(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            dj_login(request, user)
            return render(request, 'f_home/contribution.html')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('post-create'))
        else:
            messages.error(
                request, f'Invalid user or password for {username}!')

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def not_found_view(request, exception):
    return render(request, 'users/404_not_found.html')
