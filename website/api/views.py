from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_swagger.views import get_swagger_view

from portfolio.models import Project, PersonalInfo, Language, Education, Interest, Job, Skill, Membership
from .serializers import ProjectSerializer,PersonalInfoSerializer, LanguageSerializer,  EducationSerializer, InterestSerializer, JobSerializer, SkillSerializer, MembershipSerializer

api_swagger = get_swagger_view(title='API REFERENCE')



# API Response
class ProjectApiView(APIView):
    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class PersonalInfoApiView(APIView):

    def get(self, request):
        infos = PersonalInfo.objects.all()
        serializer = PersonalInfoSerializer(infos, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class LanguageApiView(APIView):
    
    def get(self, request):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class InterestApiView(APIView):
    
    def get(self, request):
        interests = Interest.objects.all()
        serializer = InterestSerializer(interests, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class EducationApiView(APIView):
    
    def get(self, request):
        educations = Education.objects.all()
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class JobApiView(APIView):
    
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

class SkillApiView(APIView):
    
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

class MembershipApiView(APIView):
    
    def get(self, request):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass