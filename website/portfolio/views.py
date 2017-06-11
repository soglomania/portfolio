from django.shortcuts import render
from django.views import generic
from functools import reduce
import operator
from django.db.models import Q

from .models import Project

class ProjectListView(generic.ListView):
    template_name='portfolio/project_list.html'
    context_object_name = 'all_projects'
    paginate_by = 4


    def get_queryset(self):
        #TODO
        # sort by most viewed or recently add first
        result = Project.objects.all() 

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
                       (Q(description__icontains=q) for q in query_list))
            )

        return result  


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    