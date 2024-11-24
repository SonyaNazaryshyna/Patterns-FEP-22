import httpx
from fastapi import APIRouter, HTTPException
import backend.api.routes.nba.utils as utils
from backend.config import HEADERS
from backend.models.api_models import PlayerSchema, GameSchema

GAMES_NBA_API_URL = "https://api.balldontlie.io/v1/games"

games_router = APIRouter(include_in_schema=True)

@games_router.get("/games", response_model=list[GameSchema])
async def get_players():
    try:
        url = utils.build_api_query(GAMES_NBA_API_URL, "")
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=HEADERS)
            response.raise_for_status()
        games_data = response.json().get("data", [])
        games = [GameSchema(**game) for game in games_data]
        return games
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"External API error: {e}")

