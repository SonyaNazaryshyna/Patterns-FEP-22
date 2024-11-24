from fastapi import FastAPI
from contextlib import asynccontextmanager

from starlette.middleware.cors import CORSMiddleware

from backend.db.database import DBConnection

from beanie import init_beanie

from backend.api.routes import router as main_router


def app_factory(lifespan):
    """Application Factory"""
    app = FastAPI(title="NBA", lifespan=lifespan)
    app.include_router(main_router)

    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    DbConnection = DBConnection()
    DbConnection.connect()
    yield
    DbConnection.sessio.close()

app = app_factory(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

