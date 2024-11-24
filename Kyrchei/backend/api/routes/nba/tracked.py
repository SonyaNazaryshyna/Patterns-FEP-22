import httpx
from fastapi import APIRouter, HTTPException
import backend.api.routes.nba.utils as utils
from backend.config import HEADERS
from backend.db.crud import *
from backend.models.api_models import TeamSchema

tracked_router = APIRouter(include_in_schema=True)


@tracked_router.get("/track", response_model=list[TeamSchema])
async def get_tracked():
    teams = read_teams()
    if not teams:
        raise HTTPException(status_code=404, detail="No tracked teams found")
    return teams
