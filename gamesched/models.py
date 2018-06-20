from django.db import models
import datetime

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
    def is_valid_to_save(home, away, date):
        if not home.isdigit():
            return False
        if not away.isdigit():
            return False
        if not isinstance(date, datetime.date):
            return False
        if away == home:
            return False
        return true
    def __str__(self):
        return self.name
    
    
        

class TeamList(models.Model):
    def getList():
        return Team.objects.all()
    
    

