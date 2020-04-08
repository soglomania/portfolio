from rest_framework import serializers
from . import models


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Biography
        fields = '__all__'


class BiographySerializerEnglish(serializers.ModelSerializer):
    job_title = serializers.CharField(source="job_title_en")
    summary = serializers.CharField(source="summary_en")
    description = serializers.CharField(source="description_en")

    class Meta:
        model = models.Biography
        fields = ["surname", "lastname", "firstname", "name", "date_of_birth", "age", "address", "phone_number", "email", "job_title", "summary", "description", "youtube", "facebook", "github", "linkedin", "viadeo", "twitter"]
        

class BiographySerializerFrench(serializers.ModelSerializer):
    job_title = serializers.CharField(source="job_title_fr")
    summary = serializers.CharField(source="summary_fr")
    description = serializers.CharField(source="description_fr")

    class Meta:
        model = models.Biography
        fields = ["surname", "lastname", "firstname", "name", "date_of_birth", "age", "address", "phone_number", "email", "job_title", "summary", "description", "youtube", "facebook", "github", "linkedin", "viadeo", "twitter"]
        


class BiographySerializerSpanish(serializers.ModelSerializer):
    job_title = serializers.CharField(source="job_title_es")
    summary = serializers.CharField(source="summary_es")
    description = serializers.CharField(source="description_es")

    class Meta:
        model = models.Biography
        fields = ["surname", "lastname", "firstname", "name", "date_of_birth", "age", "address", "phone_number", "email", "job_title", "summary", "description", "youtube", "facebook", "github", "linkedin", "viadeo", "twitter"]
        


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = '__all__'



class LanguageSerializerEnglish(serializers.ModelSerializer):

    name = serializers.CharField(source="name_en")
    level = serializers.CharField(source="level_en")
    summary = serializers.CharField(source="summary_en")
    description = serializers.CharField(source="description_en")

    class Meta:
        model = models.Language
        fields = ["name", "start_date", "level", "summary", "description"]



class LanguageSerializerFrench(serializers.ModelSerializer):
    
    name = serializers.CharField(source="name_fr")
    level = serializers.CharField(source="level_fr")
    summary = serializers.CharField(source="summary_fr")
    description = serializers.CharField(source="description_fr")

    class Meta:
        model = models.Language
        fields = ["name", "start_date", "level", "summary", "description"]



class LanguageSerializerSpanish(serializers.ModelSerializer):
    
    name = serializers.CharField(source="name_es")
    level = serializers.CharField(source="level_es")
    summary = serializers.CharField(source="summary_es")
    description = serializers.CharField(source="description_es")

    class Meta:
        model = models.Language
        fields = ["name", "start_date", "level", "summary", "description"]




class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'




class EducationSerializerEnglish(serializers.ModelSerializer):

    name = serializers.CharField(source="name_en")
    school = serializers.CharField(source="school_en")
    summary = serializers.CharField(source="summary_en")
    description = serializers.CharField(source="description_en")

    class Meta:
        model = models.Education
        fields = ["name", "start_date", "end_date", "is_current", "school", "summary", "description", "link"]



class EducationSerializerFrench(serializers.ModelSerializer):
    
    name = serializers.CharField(source="name_fr")
    school = serializers.CharField(source="school_fr")
    summary = serializers.CharField(source="summary_fr")
    description = serializers.CharField(source="description_fr")

    class Meta:
        model = models.Education
        fields = ["name", "start_date", "end_date", "is_current", "school", "summary", "description", "link"]




class EducationSerializerSpanish(serializers.ModelSerializer):
    
    name = serializers.CharField(source="name_es")
    school = serializers.CharField(source="school_es")
    summary = serializers.CharField(source="summary_es")
    description = serializers.CharField(source="description_es")

    class Meta:
        model = models.Education
        fields = ["name", "start_date", "end_date", "is_current", "school", "summary", "description", "link"]





class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'



class ExperienceSerializerEnglish(serializers.ModelSerializer):

    title = serializers.CharField(source="title_en")
    summary = serializers.CharField(source="summary_en")
    description = serializers.CharField(source="description_en")

    class Meta:
        model = models.Experience
        fields = ["title", "start_date", "end_date", "is_current", "company", "summary", "description", "link"]



class ExperienceSerializerFrench(serializers.ModelSerializer):
    
    title = serializers.CharField(source="title_fr")
    summary = serializers.CharField(source="summary_fr")
    description = serializers.CharField(source="description_fr")

    class Meta:
        model = models.Experience
        fields = ["title", "start_date", "end_date", "is_current", "company", "summary", "description", "link"]




class ExperienceSerializerSpanish(serializers.ModelSerializer):
    
    title = serializers.CharField(source="title_es")
    summary = serializers.CharField(source="summary_es")
    description = serializers.CharField(source="description_es")

    class Meta:
        model = models.Experience
        fields = ["title", "start_date", "end_date", "is_current", "company", "summary", "description", "link"]





class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = '__all__'


class SkillSerializerEnglish(serializers.ModelSerializer):
    name = serializers.CharField(source="name_en")
    summary = serializers.CharField(source="summary_en")
    description = serializers.CharField(source="description_en")
    
    class Meta:
        model = models.Skill
        fields = ["name", "summary", "description"]



class SkillSerializerFrench(serializers.ModelSerializer):
    name = serializers.CharField(source="name_fr")
    summary = serializers.CharField(source="summary_fr")
    description = serializers.CharField(source="description_fr")
    
    class Meta:
        model = models.Skill
        fields = ["name", "summary", "description"]


class SkillSerializerSpanish(serializers.ModelSerializer):
    name = serializers.CharField(source="name_es")
    summary = serializers.CharField(source="summary_es")
    description = serializers.CharField(source="description_es")
    
    class Meta:
        model = models.Skill
        fields = ["name", "summary", "description"]



class InterestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Interest
        fields = '__all__'



class InterestSerializerEnglish(serializers.ModelSerializer):

    name = serializers.CharField(source="name_en")
    summary = serializers.CharField(source="summary_en")
    description = serializers.CharField(source="description_en")
    
    class Meta:
        model = models.Interest
        fields = ["name", "summary", "description"]



class InterestSerializerFrench(serializers.ModelSerializer):
    
    name = serializers.CharField(source="name_fr")
    summary = serializers.CharField(source="summary_fr")
    description = serializers.CharField(source="description_fr")
    
    class Meta:
        model = models.Interest
        fields = ["name", "summary", "description"]


class InterestSerializerSpanish(serializers.ModelSerializer):
    
    name = serializers.CharField(source="name_es")
    summary = serializers.CharField(source="summary_es")
    description = serializers.CharField(source="description_es")
    
    class Meta:
        model = models.Interest
        fields = ["name", "summary", "description"]