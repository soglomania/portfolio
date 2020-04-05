from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project
from .serializers import ProjectSerializer, ProjectSerializerEnglish, ProjectSerializerFrench, ProjectSerializerSpanish


class ProjectApiView(APIView):
    
    def get(self, request):

        projects = Project.objects.all()

        serializer = ProjectSerializerEnglish(projects, many=True)

        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                serializer = ProjectSerializerSpanish(projects, many=True)
            if "fr" in locales:
                serializer = ProjectSerializerFrench(projects, many=True)
            if "*" in locales:
                serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)
        


