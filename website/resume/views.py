from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_swagger.views import get_swagger_view

from .models import PersonalInfo, Language, Education, Interest, Job, Skill, Membership
from .serializers import PersonalInfoSerializer, LanguageSerializer,  EducationSerializer, InterestSerializer, JobSerializer, SkillSerializer, MembershipSerializer

api_swagger = get_swagger_view(title='API REFERENCE')

class PersonalInfoView(APIView):

    def get(self, request):
        infos = PersonalInfo.objects.all()
        serializer = PersonalInfoSerializer(infos, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class LanguageView(APIView):
    
    def get(self, request):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class InterestView(APIView):
    
    def get(self, request):
        interests = Interest.objects.all()
        serializer = InterestSerializer(interests, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class EducationView(APIView):
    
    def get(self, request):
        educations = Education.objects.all()
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class JobView(APIView):
    
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

class SkillView(APIView):
    
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

class MembershipView(APIView):
    
    def get(self, request):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass