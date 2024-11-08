from django.contrib import admin
from core.models import CustomUser, Trip, Ticket


admin.site.register(CustomUser)
admin.site.register(Trip)
admin.site.register(Ticket)