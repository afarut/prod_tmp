from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from core.serialazer import TripSerialazer, TicketSerialazer, TelegramAuthSerializer
from core.models import Trip, Ticket
from django.contrib.auth import login
from django.conf import settings
from core.utils import verify_telegram_auth
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status


User = get_user_model()

# Create your views here.
class TripRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TripSerialazer
    queryset = Trip.objects.all()
    permission_classes = []


class TripCreateOrListAPIView(CreateAPIView, ListAPIView):
    serializer_class = TripSerialazer
    queryset = Trip.objects.all()
    permission_classes = []


class TicketCreateOrListAPIView(CreateAPIView, ListAPIView):
    serializer_class = TicketSerialazer
    queryset = Ticket.objects.all()
    permission_classes = []


class TicketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerialazer
    queryset = Ticket.objects.all()
    permission_classes = []

class TelegramAuthView(APIView):
    serializer_class = TelegramAuthSerializer
    def post(self, request):
        serializer = TelegramAuthSerializer(data=request.data)
        
        if serializer.is_valid():
            data = serializer.validated_data
            
            # Проверка подлинности данных
            if not verify_telegram_auth(data, settings.TELEGRAM_BOT_TOKEN):
                return Response({"detail": "Неверные данные Telegram"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Получаем или создаем пользователя
            user, created = User.objects.get_or_create(username=data["username"], defaults={"id": data["id"]})
            
            # Выполняем вход
            login(request, user)
            
            return Response({"detail": "Успешная авторизация"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
