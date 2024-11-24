from django.urls import path
from . import views

urlpatterns = [
    path('teams', views.teams_view, name='teams'),
    path('players', views.players_view, name='players'),
    path('games', views.games_view, name='games'),
    path('', views.teams_view, name= 'teams'),
    path('track', views.track_view, name='track'),
    path('rteams', views.teams_view, name='read-teams'),
    path('save',views.add_to_db, name="save-team"),
    path('save_player', views.add_player_to_d, name='save-player'),
    path('dteams', views.delete_team, name='delete-team'),
    path('dplayers', views.delete_player, name='delete-player')
]
