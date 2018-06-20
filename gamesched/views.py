from django.shortcuts import  render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.template import loader
from .models import Team
from .models import ScheduledGame

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
   return HttpResponse(template.render({'teams':Team.objects.all()}, request))   

def team_add_form(request):
    try:
       new_team_name = request.POST['teamname']
    except ():
       return render(request, 'gamesched/team_page.html', {'errmsg':'couldnt get from POST'})
    else:
       newteam = Team(name=new_team_name)
       newteam.save()
       return HttpResponseRedirect(reverse('gamesched:team_main_page'))

def process_team_schedule_a_game(request):
    try:
       hteam = get_object_or_404(Team, pk=request.POST['home'])
       ateam = get_object_or_404(Team, pk=request.POST['away'])
       frm_game_date = request.POST['gamedate']
    except ():
       return render(request, 'gamesched/team_add_form', {'errmsg':'couldnt get from POST'})
    else:
       sg = ScheduledGame(home_team=hteam,
                          away_team=ateam,
                          play_date=frm_game_date,
                          home_score = 0,
                          away_score= 0)
       sg.save();
       template = loader.get_template('gamesched/index.html')
       return HttpResponseRedirect(reverse('gamesched:team_schedule_list'))

def team_schedule_list(request):
   template = loader.get_template('gamesched/team_schedule_list.html')
   return HttpResponse(template.render({}, request))


    



