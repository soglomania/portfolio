from django.shortcuts import render, redirect
from django.utils import translation
from django.views import generic


def index(request):
    return render(request, 'home/index.html')

def set_french(request):
    user_language = 'fr'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return redirect('/')


def set_english(request):
    user_language = 'en'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return redirect('/')


def set_spanish(request):
    user_language = 'es'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return redirect('/')


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")



    