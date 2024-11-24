from typing import List

import httpx
from fastapi import APIRouter, HTTPException, Form
import backend.api.routes.nba.utils as utils
from backend.config import HEADERS
from backend.db.crud import add_player_to_db, add_team_to_db, read_teams, read_players, delete_team_from_db, \
    delete_player_from_db
from backend.models.api_models import PlayerSchema, TeamSchema, Team

db_router = APIRouter(include_in_schema=True)

@db_router.get("/rteams", response_model=List[TeamSchema])
async def get_teams():
    # delete_team_from_db("13")
    teams = await read_teams()
    return teams

@db_router.get("/rplayers", response_model=list[PlayerSchema])
async def read_playerss():
    players = read_players()
    return players

@db_router.post("/aplayers")
async def add_player(player: PlayerSchema):
    try:
        result = add_player_to_db(player.model_dump())
        return {"message": "Player added successfully", "player_id": result.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding player: {e}")

@db_router.post("/ateams")
async def add_team(team: TeamSchema):
    try:
        result = await add_team_to_db(team.dict())
        return {"message": "Team added successfully", "team_id": result.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding team: {e}")



@db_router.post("/dteams")
async def delete_teams(request):
    try:
        if request.method == 'POST':
            team_id = request.POST.get("team_id")
            print(team_id)
            result = delete_team_from_db(team_id)
        return {"message": "Team deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting team: {e}")

@db_router.post("/dplayers")
async def delete_players(request):
    try:
        if request.method == 'POST':
            team_id = request.POST.get("team_id")
            print(team_id)
            result = delete_player_from_db(team_id)
        return {"message": "Player deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting team: {e}")