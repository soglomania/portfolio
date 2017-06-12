from django.shortcuts import render, redirect
from django.utils import translation
from django.views import generic

from resume.models import PersonalInfo, Language, Interest, Skill, Job, Education, Membership

def index(request):
    
    personal_info = PersonalInfo.objects.all()[0]
    languages = Language.objects.all()
    interests = Interest.objects.all()
    skills = Skill.objects.all()
    jobs = Job.objects.all()
    educations = Education.objects.all()
    memberships = Membership.objects.all()
    
    template_name = 'home/index.html'
    context = {
        'personal_info' : personal_info,
        'languages' : languages,
        'interests' : interests,
        'skills' :skills,
        'jobs' : jobs,
        'educations' : educations,
        'memberships' : memberships,
    }

    return render(request, template_name, context)

# to render robot.txt and human.txt (remove 'fr', 'en', 'es' from url )

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")


#persist user language preference in cookie and redirect to home page

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



    