from rest_framework import serializers
from core.models import Testemonials


class ListTestemonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testemonials
        exclude = ("created_at", 'updated_at', "is_deleted", "deleted_at")