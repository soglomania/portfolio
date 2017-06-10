from django.shortcuts import render
from django.views import generic

from .models import Project

class ProjectListView(generic.ListView):
    template_name='portfolio/project_list.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Project.objects.all()    


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    




