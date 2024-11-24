import httpx
from fastapi import APIRouter, HTTPException
import backend.api.routes.nba.utils as utils
from backend.config import HEADERS
from backend.models.api_models import PlayerSchema


PLAYERS_NBA_API_URL = "https://api.balldontlie.io/v1/players"

players_router = APIRouter(include_in_schema=True)

@players_router.get("/players", response_model=list[PlayerSchema])
async def get_players():
    try:
        url = utils.build_api_query(PLAYERS_NBA_API_URL, "")
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=HEADERS)
            response.raise_for_status()
        players_data = response.json().get("data", [])
        players = [
            PlayerSchema(
                id=player['id'],
                first_name=player['first_name'],
                last_name=player['last_name'],
                position=player['position'],
                height=player['height'],
                weight=player['weight'],
                jersey_number=player['jersey_number'],
                college=player.get('college'),
                country=player['country'],
                draft_year=player.get('draft_year'),
                draft_round=player.get('draft_round'),
                draft_number=player.get('draft_number'),
                team=player.get('team', {}).get('abbreviation') if player.get('team') else None
            )
            for player in players_data
        ]
        return players
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"External API error: {e}")