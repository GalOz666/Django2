from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse, get_object_or_404
# from .models import model, model
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView


# Create your views here.

def index(request):
    return render(request, 'index.html')


def other_page(request):
    relativedict = {"wtf": 'WTF', 'number': 666}
    return render(request, 'other.html', context=relativedict)


def relative(request):
    relativedict = {"wtf": 'WTF', 'number': 100, 'hello': 'hello you motherfucking piece of shit'}
    return render(request, 'other.html', context=relativedict)


# @require_http_methods(['POST'])
def login_page(request):
    context = {"user_login": forms.UserForm}
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        HttpResponseRedirect(request, reverse('index'), context={})

    else:
        render(request, "relative.html", context=context)


def register(request):
    registered = False

    if request.method == 'POST':
        user_regis = forms.UserForm(request.POST)
        profile_form = forms.ProfileForm(request.POST)
        if profile_form.is_valid and user_regis.is_valid:
            user_regis.save()
            user_regis.set_password(user_regis.password)
            user_regis.save()

            profile = profile_form.save(commit=False)

            # Check if they provided a profile picture

            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()
                registered = True

        else:
            print(user_regis.errors, profile_form.errors)
    return render(request, 'basic_app/login.html', context={"user_form": forms.UserForm, "profile_form": forms.ProfileForm, "registered": registered})