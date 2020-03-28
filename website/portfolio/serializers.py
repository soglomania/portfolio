from rest_framework import serializers
from .models import Project, PersonalInfo, Language, Education, Interest, Job, Skill, Membership


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class PersonalInfoSerializerEnglish(serializers.ModelSerializer):
    job_title = serializers.CharField(source="job_title_en")
    summary = serializers.CharField(source="summary_en")
    intro_url = serializers.CharField(source="intro_url_en")

    class Meta:
        model = PersonalInfo
        fields = ["surname", "firstname", "age", "address", "phone_number", "email", "job_title", "summary", "intro_url"]
        

class PersonalInfoSerializerFrench(serializers.ModelSerializer):
    job_title = serializers.CharField(source="job_title_fr")
    summary = serializers.CharField(source="summary_fr")
    intro_url = serializers.CharField(source="intro_url_fr")

    class Meta:
        model = PersonalInfo
        fields = ["surname", "firstname", "age", "address", "phone_number", "email", "job_title", "summary", "intro_url"]
        


class PersonalInfoSerializerSpanish(serializers.ModelSerializer):
    job_title = serializers.CharField(source="job_title_es")
    summary = serializers.CharField(source="summary_es")
    intro_url = serializers.CharField(source="intro_url_es")

    class Meta:
        model = PersonalInfo
        fields = ["surname", "firstname", "age", "address", "phone_number", "email", "job_title", "summary", "intro_url"]
        


class LanguageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Language
        fields = '__all__'



class InterestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Interest
        fields = '__all__'



class EducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Education
        fields = '__all__'



class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = '__all__'



class MembershipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Membership
        fields = '__all__'