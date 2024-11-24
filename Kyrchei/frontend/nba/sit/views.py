import os
import sys
from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sqlalchemy.sql.sqltypes import NULLTYPE

from backend.db.crud import add_player_to_db, add_team_to_db, delete_team_from_db, delete_player_from_db
from frontend.nba.sit.models import TileFactory

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

def teams_view(request):
    try:
        response = requests.get(f'{BASE_URL}/teams')
        response.raise_for_status()
        teams = response.json()
        team_tiles = [TileFactory.create_team_tile(team) for team in teams]
        return render(request, 'teams.html', {'teams': team_tiles, 'active_tab': 'teams'})
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=500)

def players_view(request):
    try:
        response = requests.get(f'{BASE_URL}/players')
        response.raise_for_status()
        players = response.json()
        player_tiles = [TileFactory.create_player_tile(player) for player in players]
        return render(request, 'players.html', {'players': player_tiles, 'active_tab': 'players'})
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=500)

def games_view(request):
    try:
        response = requests.get(f'{BASE_URL}/games')
        response.raise_for_status()
        games = response.json()
        return render(request, 'games.html', {'games': games, 'active_tab': 'games'})
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=500)


def track_view(request):
    try:
        response = requests.get(f'{BASE_URL}/rteams')
        player_response = requests.get(f'{BASE_URL}/rplayers')
        response.raise_for_status()
        player_response.raise_for_status()
        teams = response.json()
        players = player_response.json()
        team_tiles = [TileFactory.create_team_tile(team) for team in teams]
        player_tiles = [TileFactory.create_player_tile(player) for player in players]
        if isinstance(teams, str):
            return HttpResponse(teams, status=500)
        if isinstance(teams, str):
            return HttpResponse(players, status=500)
        return render(request, 'track.html', {'teams': team_tiles, 'players': player_tiles, 'active_tab': 'checked'})
    except Exception as e:
        return HttpResponse(f"Error occurred: {str(e)}", status=500)

@csrf_exempt
def add_player_to_d(request):
    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        player_first_name = request.POST.get('player_first_name')
        player_last_name = request.POST.get('player_last_name')
        player_position = request.POST.get('player_position')
        player_height = request.POST.get('player_height')
        player_weight = request.POST.get('player_weight')
        player_jersey = request.POST.get('player_jersey')
        player_college = request.POST.get('player_college')
        player_country = request.POST.get('player_country')
        player_draft_year = request.POST.get('player_draft_year')
        player_draft_round = request.POST.get('player_draft_round')
        player_draft_number = request.POST.get('player_draft_number')
        player_team_id = request.POST.get('player_team')


        player_data = {
            'id': int(player_id) if player_id else None,
            'first_name': player_first_name,
            'last_name': player_last_name,
            'position': player_position,
            'height': player_height,
            'weight': player_weight,
            'jersey_number': player_jersey,
            'college': player_college,
            'country': player_country,
            'draft_year': player_draft_year if player_draft_year is not None else 0,
            'draft_round': player_draft_round if player_draft_round is not None else 0,
            'draft_number': player_draft_number if player_draft_number is not None else 0,
            'team_id': player_team_id
        }

        result = add_player_to_db(player_data)
        return JsonResponse({'message': result})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def add_to_db(request):
    if request.method == 'POST':
        team_id = request.POST.get('team_id')
        team_name = request.POST.get('team_name')
        team_city = request.POST.get('team_city')
        team_division = request.POST.get('team_division')
        team_conference = request.POST.get('team_conference')

        team_data = {
            'id': team_id,
            'name': team_name,
            'city': team_city,
            'division': team_division,
            'conference': team_conference
        }
        result = add_team_to_db(team_data)
        return JsonResponse({'message': result})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def delete_team(request):
    if request.method == 'POST':
        team_id = request.POST.get("team_id")
        print(team_id)
        result = delete_team_from_db(team_id)
        return JsonResponse({'message': result})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete_player(request):
    if request.method == 'POST':
        player_id = request.POST.get("player_id")
        print(player_id)
        result = delete_player_from_db(player_id)
        return JsonResponse({'message': result})

    return JsonResponse({'error': 'Invalid request'}, status=400)
