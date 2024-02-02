from django.urls import path
from home import views

urpatterns = [
    path('', views.my_home, name="Home"),
]