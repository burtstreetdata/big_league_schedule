from django.shortcuts import  render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.template import loader
from .models import Team

# Create your views here.

def index(request):
   template = loader.get_template('gamesched/index.html')
   return HttpResponse(template.render({'a':''}, request))

def team_main_page(request):
   template = loader.get_template('gamesched/team_main_page.html')
   return HttpResponse(template.render({}, request))

def team_add(request):
   existing_teams = Team.objects.all()
   template = loader.get_template('gamesched/team_add.html')
   return HttpResponse(template.render({'teams':existing_teams}, request))

def team_schedule_a_game(request):
   template = loader.get_template('gamesched/schedule_a_game.html')
   return HttpResponse(template.render({'teams':Team.objects.all()}))   

def team_add_form(request):
    try:
       new_team_name = request.POST['teamname']
    except ():
       return render(request, 'gamesched/team_page.html', {'errmsg':'couldnt get from POST'})
    else:
       newteam = Team(name=new_team_name)
       newteam.save()
       template = loader.get_template('gamesched/team_main_page.html')
       return HttpResponseRedirect(reverse('gamesched:team_main_page'))

def PROCESS_team_schedule_a_game(request):
 return HttpResponse("stub")


