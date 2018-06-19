from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ScheduledGame(models.Model):
    play_date = models.DateField('day scheduled')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away')
    home_score = models.IntegerField()
    away_score = models.IntegerField()

class TeamList(models.Model):

    def getList():
        return Team.objects.all()
    
    

