# elly_stats_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the Django admin site
    path('player_stats/', include('player_stats.urls')),  # Include the player_stats app URLs
]
