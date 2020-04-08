from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers 


class BiographyApiView(APIView):
    
    def get(self, request):

        biography = models.Biography.objects.all()[:1].get()
        
        serializer = serializers.BiographySerializerEnglish(biography, many=False)

        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                serializer = serializers.BiographySerializerSpanish(biography, many=False)
            if "fr" in locales:
                serializer = serializers.BiographySerializerFrench(biography, many=False)
            if "*" in locales:
                serializer = serializers.BiographySerializer(biography, many=False)

        return Response(serializer.data)


class LanguageApiView(APIView):
    
    def get(self, request):

        languages = models.Language.objects.all()

        serializer = serializers.LanguageSerializerEnglish(languages, many=True)

        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                serializer = serializers.LanguageSerializerSpanish(languages, many=True)
            if "fr" in locales:
                serializer = serializers.LanguageSerializerFrench(languages, many=True)
            if "*" in locales:
                serializer = serializers.LanguageSerializer(languages, many=True)

        return Response(serializer.data)
        



class EducationApiView(APIView):
    
    def get(self, request):
        educations = models.Education.objects.all()

        serializer = serializers.EducationSerializerEnglish(educations, many=True)

        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                serializer = serializers.EducationSerializerSpanish(educations, many=True)
            if "fr" in locales:
                serializer = serializers.EducationSerializerFrench(educations, many=True)
            if "*" in locales:
                serializer = serializers.EducationSerializer(educations, many=True)

        return Response(serializer.data)




class ExperienceApiView(APIView):
    
    def get(self, request):

        experiences = models.Experience.objects.all()

        serializer = serializers.ExperienceSerializerEnglish(experiences, many=True)

        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                serializer = serializers.ExperienceSerializerSpanish(experiences, many=True)
            if "fr" in locales:
                serializer = serializers.ExperienceSerializerFrench(experiences, many=True)
            if "*" in locales:
                serializer = serializers.ExperienceSerializer(experiences, many=True)

        return Response(serializer.data)



class SkillApiView(APIView):
    
    def get(self, request):

        skills = models.Skill.objects.all()

        serializer = serializers.SkillSerializerEnglish(skills, many=True)

        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                serializer = serializers.SkillSerializerSpanish(skills, many=True)
            if "fr" in locales:
                serializer = serializers.SkillSerializerFrench(skills, many=True)
            if "*" in locales:
                serializer = serializers.SkillSerializer(skills, many=True)

        return Response(serializer.data)



class InterestApiView(APIView):
    
    def get(self, request):

        interests = models.Interest.objects.all()

        serializer = serializers.InterestSerializerEnglish(interests, many=True)

        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                serializer = serializers.InterestSerializerSpanish(interests, many=True)
            if "fr" in locales:
                serializer = serializers.InterestSerializerFrench(interests, many=True)
            if "*" in locales:
                serializer = serializers.InterestSerializer(interests, many=True)

        return Response(serializer.data)
        



class ResumeApiView(APIView):
    
    def get(self, request):

        biography = models.Biography.objects.all()[:1].get()
        biography_serializer = serializers.BiographySerializerEnglish(biography, many=False)

        languages = models.Language.objects.all()
        languages_serializer = serializers.LanguageSerializerEnglish(languages, many=True)


        educations = models.Education.objects.all()
        educations_serializer = serializers.EducationSerializerEnglish(educations, many=True)

        experiences = models.Experience.objects.all()
        experiences_serializer = serializers.ExperienceSerializerEnglish(experiences, many=True)

        skills = models.Skill.objects.all()
        skills_serializer = serializers.SkillSerializerEnglish(skills, many=True)

        interests = models.Interest.objects.all()
        interests_serializers = serializers.InterestSerializerEnglish(interests, many=True)


        locales = self.request.META.get("HTTP_ACCEPT_LANGUAGE")
        if locales:
            if "es" in locales:
                biography_serializer = serializers.BiographySerializerSpanish(biography, many=False)
                languages_serializer = serializers.LanguageSerializerSpanish(languages, many=True)
                educations_serializer = serializers.EducationSerializerSpanish(educations, many=True)
                experiences_serializer = serializers.ExperienceSerializerSpanish(experiences, many=True)
                skills_serializer = serializers.SkillSerializerSpanish(skills, many=True)
                interests_serializers = serializers.InterestSerializerSpanish(interests, many=True)

            if "fr" in locales:
                biography_serializer = serializers.BiographySerializerFrench(biography, many=False)
                languages_serializer = serializers.LanguageSerializerFrench(languages, many=True)
                educations_serializer = serializers.EducationSerializerFrench(educations, many=True)
                experiences_serializer = serializers.ExperienceSerializerFrench(experiences, many=True)
                skills_serializer = serializers.SkillSerializerFrench(skills, many=True)
                interests_serializers = serializers.InterestSerializerFrench(interests, many=True)

            if "*" in locales:
                biography_serializer = serializers.BiographySerializer(biography, many=False)
                languages_serializer = serializers.LanguageSerializer(languages, many=True)
                educations_serializer = serializers.EducationSerializer(educations, many=True)
                experiences_serializer = serializers.ExperienceSerializer(experiences, many=True)
                skills_serializer = serializers.SkillSerializer(skills, many=True)
                interests_serializers = serializers.InterestSerializer(interests, many=True)
        

        response = {
            "biography" : biography_serializer.data,
            "languages" : languages_serializer.data,
            "educations": educations_serializer.data,
            "experiences": experiences_serializer.data,
            "skills": skills_serializer.data,
            "interests": interests_serializers.data,
        }

        return Response(response)

