from django.db import models
#from .constants import VERBOSE_STATUS_TYPE
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Trip(models.Model):
    # status = models.PositiveSmallIntegerField(choices=VERBOSE_STATUS_TYPE)
    # price = models.PositiveIntegerField()
    title = models.CharField(max_length=100)

class CustomUser(AbstractUser):
    hometown = models.CharField(max_length=100, default="")
    telegram_chat_id = models.IntegerField(default=0)
    

class Ticket(models.Model):
    user = models.ForeignKey(CustomUser,
                            on_delete=models.CASCADE,
                            related_name="tickets",)
    trip = models.ForeignKey(Trip,
                            on_delete=models.CASCADE,
                            related_name="tickets",)