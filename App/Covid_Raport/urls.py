from django.urls import path, include
from .views import Home_covid,Country_detalis

urlpatterns = [

    path('',Home_covid),
    path('details/<country>',Country_detalis)
]
