from django.contrib import admin
from django.urls import path, include
from player_stats import views as player_views  # ADD this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('player_stats/', include('player_stats.urls')),
    path('signup/', player_views.signup_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout
]
