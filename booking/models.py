from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


SERVICE_CHOICES = (
    ("One vs One", "One vs One"),
    ("Defending Training", "Defending Training"),
    ("Finnishing and Passing", "Finnishing and Passing"),
    ("Teknik and Dribbling", "Teknik and Dribbling"),
    )

TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("5 PM", "5 PM"),
    ("7 PM", "7 PM"),
)

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="One vs One")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"