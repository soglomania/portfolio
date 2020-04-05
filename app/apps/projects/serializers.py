from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class ProjectSerializerEnglish(serializers.ModelSerializer):
    category = serializers.CharField(source="category_en")
    summary = serializers.CharField(source="summary_en")
    description = serializers.CharField(source="description_en")

    class Meta:
        model = Project
        fields = ["title", "logo", "category", "summary", "description", "link", "github"]
    


class ProjectSerializerFrench(serializers.ModelSerializer):
    category = serializers.CharField(source="category_fr")
    summary = serializers.CharField(source="summary_fr")
    description = serializers.CharField(source="description_fr")

    class Meta:
        model = Project
        fields = ["title", "logo", "category", "summary", "description", "link", "github"]


class ProjectSerializerSpanish(serializers.ModelSerializer):
    category = serializers.CharField(source="category_es")
    summary = serializers.CharField(source="summary_es")
    description = serializers.CharField(source="description_es")

    class Meta:
        model = Project
        fields = ["title", "logo", "category", "summary", "description", "link", "github"]