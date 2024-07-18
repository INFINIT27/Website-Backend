from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Classes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"passowrd": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ["id", "class_number", "class_name", "class_description", "author"]
        extra_kwargs = {"author": {"read_only": True}}