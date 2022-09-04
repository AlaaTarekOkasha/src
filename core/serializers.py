from dataclasses import field
from pdb import post_mortem
from statistics import mode
from rest_framework import serializers
from .models import *


class ListTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class ListTestemonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testemonial
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    content_list = serializers.StringRelatedField(many=True)
    end_content_list = serializers.StringRelatedField(many=True)
    user_criteria_list = serializers.StringRelatedField(many=True)
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'description',
            'image',
            'price',
            'hours',
            'start_date',
            'content_list',
            'end_content_list',
            'user_criteria_list',
        )

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = (
            'description',
        )        

class EndContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseBenefit
        fields = (
            'description',
        )


class UserCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCriteria
        fields = (
            'description',
        )

class TrainerSerializer(serializers.ModelSerializer):
    trainers_list = ListTrainerSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = (
            'trainers_list',
        )

class TestemonialSerializer(serializers.ModelSerializer):
    testemonials_list = ListTestemonialSerializer(many=True, read_only=True) 
    class Meta:
        model = Course
        fields = (
            'testemonials_list', 
        )