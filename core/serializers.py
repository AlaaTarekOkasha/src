from dataclasses import field
from pdb import post_mortem
from statistics import mode
from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'title',
            'description',
            'image',
            'price',
        )

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'content',
        )        

class EndContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'end_content',
        )


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'criteria',
        )

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'trainers_list',
        )

class TestemonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'testemonials_list',
        )