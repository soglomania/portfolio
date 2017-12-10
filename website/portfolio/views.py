import operator
from functools import reduce

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from django.views import generic

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project



class ProjectCategoryView(generic.base.TemplateView):
    template_name = 'portfolio/project_category.html'




class ProjectListView(generic.ListView):
    template_name='portfolio/project_list.html'
    context_object_name = 'all_projects'
    paginate_by = 3


    def get_queryset(self):
        #TODO: sort by most viewed or recently add first
        result = Project.objects.all() 

        query = self.request.GET.get('q')
        
        if query and len(query.strip())>0:
            self.paginate_by = 3

            query_list = query.split()
            result = result.filter(
                reduce(operator.or_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.or_,
                       (Q(summary__icontains=q) for q in query_list)) |
                reduce(operator.or_,
                       (Q(description__icontains=q) for q in query_list)) |
                reduce(operator.or_,
                       (Q(tag__icontains=q) for q in query_list))       
            )

        return result  


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'

