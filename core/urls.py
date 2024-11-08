from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path("trip/", views.TripCreateOrListAPIView.as_view(), name="trip"),
    path("trip/<int:pk>/", views.TripRetrieveUpdateDestroyAPIView.as_view(), name="trip_edit"),
    path("ticket/", views.TicketCreateOrListAPIView.as_view(), name="ticket"),
    path("ticket/<int:pk>/", views.TicketRetrieveUpdateDestroyAPIView.as_view(), name="ticket_edit"),
    path("telegram/auth/", views.TelegramAuthView.as_view(), name='telegram_auth')
]