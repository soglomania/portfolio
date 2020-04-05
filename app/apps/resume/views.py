from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Biography, Education, Interest, Job, Language, Membership, Skill)

from .serializers import (BiographySerializer, BiographySerializerEnglish, BiographySerializerFrench, BiographySerializerSpanish,
                          EducationSerializer, InterestSerializer,
                          JobSerializer, LanguageSerializer,
                          MembershipSerializer,  SkillSerializer)



class ResumeApiView(APIView):
    
    def get(self, request):

        infos = Biography.objects.all()[:1].get()

        infos_serializer = BiographySerializerEnglish(infos, many=False)
        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                infos_serializer = BiographySerializerSpanish(infos, many=False)
            if "fr" in locales:
                infos_serializer = BiographySerializerFrench(infos, many=False)
            if "*" in locales:
                infos_serializer = BiographySerializer(infos, many=False)
        

        response = {
            "biography" : infos_serializer.data,
            "languages" : [],
            "interests": [],
            "educations": [],
            "jobs": [],
            "skills": [],
            "membership": []
        }

        return Response(response)


class BiographyApiView(APIView):
    
    def get(self, request):

        infos = Biography.objects.all()[:1].get()
        
        serializer = BiographySerializerEnglish(infos, many=False)

        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                serializer = BiographySerializerSpanish(infos, many=False)
            if "fr" in locales:
                serializer = BiographySerializerFrench(infos, many=False)
            if "*" in locales:
                serializer = BiographySerializer(infos, many=False)

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
        

