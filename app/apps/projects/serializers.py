from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class ProjectSerializerEnglish(serializers.ModelSerializer):
    summary = serializers.CharField(source="summary_en")
    description = serializers.CharField(source="description_en")

    class Meta:
        model = Project
        fields = ["title", "category", "summary", "description", "link", "github"]
    


class ProjectSerializerFrench(serializers.ModelSerializer):
    summary = serializers.CharField(source="summary_fr")
    description = serializers.CharField(source="description_fr")

    class Meta:
        model = Project
        fields = ["title", "category", "summary", "description", "link", "github"]


class ProjectSerializerSpanish(serializers.ModelSerializer):
    summary = serializers.CharField(source="summary_es")
    description = serializers.CharField(source="description_es")

    class Meta:
        model = Project
        fields = ["title", "category", "summary", "description", "link", "github"]