from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Education, Interest, Job, Language, Membership,
                     PersonalInfo, Project, Skill)
from .serializers import (EducationSerializer, InterestSerializer,
                          JobSerializer, LanguageSerializer,
                          MembershipSerializer, PersonalInfoSerializer, PersonalInfoSerializerEnglish, 
                          PersonalInfoSerializerFrench, PersonalInfoSerializerSpanish,
                          ProjectSerializer, ProjectSerializer, SkillSerializer)



def api_swagger(request):
    response =  HttpResponse()
    try:
        response["Content-Type"] = "text/plain"
        response['X-Accel-Redirect'] = '/media/' + "swagger.yaml"
    except Exception:
        raise Http404
    return response



class PersonalInfoApiView(APIView):
    
    def get(self, request):

        infos = PersonalInfo.objects.all()
        
        serializer = PersonalInfoSerializerEnglish(infos, many=True)

        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                serializer = PersonalInfoSerializerSpanish(infos, many=True)
            if "fr" in locales:
                serializer = PersonalInfoSerializerFrench(infos, many=True)
            if "*" in locales:
                serializer = PersonalInfoSerializer(infos, many=True)

        return Response(serializer.data)


class ProjectApiView(APIView):
    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
        



        


class LanguageApiView(APIView):
    
    def get(self, request):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)
        


class InterestApiView(APIView):
    
    def get(self, request):
        interests = Interest.objects.all()
        serializer = InterestSerializer(interests, many=True)
        return Response(serializer.data)
        


class EducationApiView(APIView):
    
    def get(self, request):
        educations = Education.objects.all()
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)
        


class JobApiView(APIView):
    
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
        

class SkillApiView(APIView):
    
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
        

class MembershipApiView(APIView):
    
    def get(self, request):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)
        

