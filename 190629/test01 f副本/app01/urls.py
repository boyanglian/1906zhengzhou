from django.urls import path
from app01.views import *

app_name = "app01"
urlpatterns = [
    path('index/', index),
]
