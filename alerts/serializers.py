from rest_framework import serializers
from .models import Alert


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'user', 'coin', 'target_price', 'current_price', 'status', 'created_at', 'updated_at')
        read_only_fields = ('user', 'status', 'created_at', 'updated_at')
