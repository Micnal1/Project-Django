from django.urls import path, include
from .views import Home_covid

urlpatterns = [

    path('',Home_covid)
]
