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



class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'content',
        )        

class EndContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'course_benefits',
        )


class UserCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'user_criteria',
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

class CourseSerializer(serializers.ModelSerializer):
    trainers_list = ListTrainerSerializer(many=True, read_only=True)
    testemonials_list = ListTestemonialSerializer(many=True, read_only=True) 
    class Meta:
        model = Course
        fields = (
            'slug',
            'id',
            'title',
            'description',
            'image',
            'price',
            'hours',
            'start_date',
            'content',
            'course_benefits',
            'user_criteria',
            'trainers_list',
            'testemonials_list'
        )



class SlugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'slug',
        )
