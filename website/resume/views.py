from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonalInfo, Language, Education, Interest, Job, Skill, Membership
from .serializers import PersonalInfoSerializer, LanguageSerializer,  EducationSerializer, InterestSerializer, JobSerializer, SkillSerializer, MembershipSerializer



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