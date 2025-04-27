# player_stats/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('elly_stats/', views.view_elly_stats, name='elly_stats'),  # URL for Elly's stats page
]
