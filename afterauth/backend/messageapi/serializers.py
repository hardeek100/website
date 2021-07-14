from rest_framework import serializers
from .models import Message

class MessageSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "name", "email", "description")
        