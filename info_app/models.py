from django.db import models

# Create your models here.


class TeamInfo(models.Model):
    name = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)
    number_of_champ = models.IntegerField()

class PlayerInfo(models.Model):
    team_id = models.IntegerField()
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    info_self = models.TextField()