from django.urls import path

from . import views

app_name = 'gamesched'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'team/add_form', views.team_add_form, name='team_add_form'),
    path(r'team/add', views.team_add, name='team_add'),
    path(r'team/schedule/PROCESS', views.PROCESS_team_schedule_a_game, name='PROCESS_team_schedule_a_game'),
    path(r'team/schedule', views.team_schedule_a_game, name='team_schedule_a_game'),
    path(r'team/', views.team_main_page, name='team_main_page'),
    ]

