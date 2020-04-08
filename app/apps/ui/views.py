import operator
from functools import reduce
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import translation
from django.views import generic

from apps.projects.models import Project as ProjectModel
from apps.resume.models import Biography as BiographyModel

from . import utils


def set_french(request):
    redirect_url = utils.parse_url(request.GET.get('next', '/'))
    user_language = 'fr'
    translation.activate(user_language)
    response = HttpResponseRedirect(redirect_url)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    return response


def set_english(request):
    redirect_url = utils.parse_url(request.GET.get('next', '/'))
    user_language = 'en'
    translation.activate(user_language)
    response = HttpResponseRedirect(redirect_url)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    return response



def set_spanish(request):
    redirect_url = utils.parse_url(request.GET.get('next', '/'))
    user_language = 'es'
    translation.activate(user_language)
    response = HttpResponseRedirect(redirect_url)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    
    return response



def index(request):
    
    biography = BiographyModel.objects.all()[:1].get()
    
    template_name = 'home/index.html'
    context = {
        'biography' : biography,
    }

    return render(request, template_name, context)


class Projects(generic.ListView):

    template_name='portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = None


    def get_queryset(self):
        
        result = ProjectModel.objects.all() 

        query = self.request.GET.get('q')
        
        if query and len(query.strip())>0:
            self.paginate_by = None

            query_list = query.split()
            result = result.filter(
                reduce(operator.or_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.or_,
                       (Q(summary__icontains=q) for q in query_list)) |
                reduce(operator.or_,
                       (Q(description__icontains=q) for q in query_list)) |
                reduce(operator.or_,
                       (Q(category__icontains=q) for q in query_list))       
            )

        return result  


    def get_context_data(self, **kwargs):

        biography = BiographyModel.objects.all()[:1].get()
        categories = ProjectModel.objects.values_list("category", flat=True).distinct()

        context = super().get_context_data(**kwargs)
        context['biography'] = biography
        context["categories"] = categories

        return context



class Project(generic.DetailView):

    model = ProjectModel
    template_name = 'portfolio/project.html'


    def get_context_data(self, **kwargs):

        biography = BiographyModel.objects.all()[:1].get()
        categories = ProjectModel.objects.values_list("category", flat=True).distinct()

        context = super().get_context_data(**kwargs)
        context['biography'] = biography
        context["categories"] = categories

        return context

