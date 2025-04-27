# player_stats/views.py

from django.shortcuts import render
from .models import PlayerStats

def view_elly_stats(request):
    # Retrieve Elly's stats from the database
    elly_stats = PlayerStats.objects.filter(player_name="Elly De La Cruz").first()

    # Check if stats exist, if not, initialize a dictionary with the default values
    if not elly_stats:
        elly_stats = {
            "player_name": "Elly De La Cruz",
            "season": 2025,
            "games_played": 20,
            "at_bats": 83,
            "hits": 20,
            "home_runs": 4,
            "runs_batted_in": 21,
            "stolen_bases": 6,
            "walks": 8,
            "strikeouts": 28,
            "doubles": 3,
            "triples": 0,
            "obp": 0.308,
            "slg": 0.410,
            "ops": 0.718,
            "iso": 0.169,
            "babip": 0.314,
            "woba": 0.318,
            "xwoba": 0.370,
            "barrel_percentage": 18.0,
            "hard_hit_percentage": 56.0,
            "avg_exit_velocity": 94.4
        }

    return render(request, 'player_stats/stats.html', {'elly_stats': elly_stats})
