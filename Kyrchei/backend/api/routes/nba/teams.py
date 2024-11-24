import httpx
from fastapi import APIRouter, HTTPException
import backend.api.routes.nba.utils as utils
from backend.config import HEADERS
from backend.db.crud import *
from backend.models.api_models import TeamSchema

TEAMS_NBA_API_URL = "https://api.balldontlie.io/v1/teams"

teams_router = APIRouter(include_in_schema=True)


@teams_router.get("/teams", response_model=list[TeamSchema])
async def get_teams():
    try:
        url = utils.build_api_query(TEAMS_NBA_API_URL, "")
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=HEADERS)
            response.raise_for_status()
        teams_data = response.json().get("data", [])
        teams = [TeamSchema(**team) for team in teams_data]

        return teams

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"External API error: {e}")

