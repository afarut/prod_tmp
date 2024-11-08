from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Trip, Ticket


User = get_user_model()

class TelegramAuthSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    auth_date = serializers.IntegerField()
    hash = serializers.CharField(max_length=64)
    photo_url = serializers.URLField(required=False, allow_blank=True)




class TripSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"


class TicketSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

        