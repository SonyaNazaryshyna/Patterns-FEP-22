from fastapi import APIRouter

from backend.api.routes.nba.db import db_router
from backend.api.routes.nba.teams import teams_router
from backend.api.routes.nba.players import players_router
from backend.api.routes.nba.games import games_router
from backend.api.routes.nba.tracked import tracked_router

router = APIRouter()


router.include_router(teams_router, prefix="", tags=["teams_router"], include_in_schema=True)
router.include_router(players_router, prefix="", tags=["players_router"], include_in_schema=True)
router.include_router(games_router, prefix="", tags=["games_router"], include_in_schema=True)
router.include_router(tracked_router, prefix="", tags=["tracked_router"], include_in_schema=True)
router.include_router(db_router, prefix="", tags=["db_router"], include_in_schema=True)