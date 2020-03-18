from rest_framework import serializers
from portfolio.models import Project, PersonalInfo, Language, Education, Interest, Job, Skill, Membership


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'



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