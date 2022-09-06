from .testmonial import ListTestemonialSerializer
from .trainer import ListTrainerSerializer
from rest_framework import serializers
from core.models import Courses


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
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
        )

class TrainerSerializer(serializers.ModelSerializer):
    trainers = ListTrainerSerializer(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = (
            'trainers',
        )

class TestemonialSerializer(serializers.ModelSerializer):
    testemonials = ListTestemonialSerializer(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = (
            'testemonials',
        )