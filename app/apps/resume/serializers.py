from rest_framework import serializers
from .models import Biography, Language, Education, Interest, Job, Skill, Membership


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class BiographySerializerEnglish(serializers.ModelSerializer):
    job_title = serializers.CharField(source="job_title_en")
    summary = serializers.CharField(source="summary_en")

    class Meta:
        model = Biography
        fields = ["surname", "firstname", "age", "address", "phone_number", "email", "job_title", "summary", "youtube", "facebook", "github", "linkedin", "viadeo", "twitter"]
        

class BiographySerializerFrench(serializers.ModelSerializer):
    job_title = serializers.CharField(source="job_title_fr")
    summary = serializers.CharField(source="summary_fr")

    class Meta:
        model = Biography
        fields = ["surname", "firstname", "age", "address", "phone_number", "email", "job_title", "summary", "youtube", "facebook", "github", "linkedin", "viadeo", "twitter"]
        


class BiographySerializerSpanish(serializers.ModelSerializer):
    job_title = serializers.CharField(source="job_title_es")
    summary = serializers.CharField(source="summary_es")

    class Meta:
        model = Biography
        fields = ["surname", "firstname", "age", "address", "phone_number", "email", "job_title", "summary", "youtube", "facebook", "github", "linkedin", "viadeo", "twitter"]
        


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