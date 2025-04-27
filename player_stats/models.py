# player_stats/models.py

from django.db import models

class PlayerStats(models.Model):
    player_name = models.CharField(max_length=100)
    season = models.IntegerField()
    games_played = models.IntegerField()
    at_bats = models.IntegerField()
    hits = models.IntegerField()
    home_runs = models.IntegerField()
    runs_batted_in = models.IntegerField()
    stolen_bases = models.IntegerField()
    walks = models.IntegerField()
    strikeouts = models.IntegerField()
    doubles = models.IntegerField()
    triples = models.IntegerField()
    obp = models.FloatField()
    slg = models.FloatField()
    ops = models.FloatField()
    iso = models.FloatField()
    babip = models.FloatField()
    woba = models.FloatField()
    xwoba = models.FloatField()
    barrel_percentage = models.FloatField()
    hard_hit_percentage = models.FloatField()
    avg_exit_velocity = models.FloatField()

    def __str__(self):
        return f"{self.player_name} - {self.season} Stats"
