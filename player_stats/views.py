# player_stats/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import PlayerStats

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('elly_stats')  # <- Redirect to stats page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def view_elly_stats(request):
    elly = PlayerStats.objects.filter(player_name="Elly De La Cruz").first()
    return render(request, 'player_stats/player_stats_list.html', {'elly': elly})
