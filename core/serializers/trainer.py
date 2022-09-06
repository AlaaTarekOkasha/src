from rest_framework import serializers
from core.models import Trainers


class ListTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainers
        exclude = ("created_at", "deleted_at", "updated_at", "is_deleted")