"""Current weather report model"""
from typing import Tuple, Optional, Union
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TeamSchema(BaseModel):
    id: int
    conference: str
    division: str
    city: str
    name: Optional[str]
    full_name: Optional[str]
    abbreviation: Optional[str]

    model_config = {'from_attributes': True}

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    conference = Column(String)
    division = Column(String)
    city = Column(String)
    name = Column(String)
    full_name = Column(String)
    abbreviation = Column(String)

    def __repr__(self) -> str:
        return f"Team({self.full_name})"

    def __repr__(self) -> str:
        return f"Team({self.full_name})"

    def __str__(self) -> str:
        return self.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Team):
            return self.id == other.id
        return False

    @property
    def created(self) -> datetime:
        """Datetime weather report was created from ID"""
        return self.d.generation_time

    @classmethod
    async def by_city(cls, id: int) -> "Team":
        """Get a weather report by city"""
        return await cls.find_one({"id": id})

class PlayerSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    position: str
    height: str
    weight: str
    jersey_number: str
    college: Optional[str]
    country: str
    draft_year: Optional[int]
    draft_round: Optional[int]
    draft_number: Optional[int]
    team: Optional[Union[TeamSchema, str]]

    model_config = {'from_attributes': True}

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    height = Column(String)
    weight = Column(String)
    jersey_number = Column(String)
    college = Column(String)
    country = Column(String)
    draft_year = Column(Integer)
    draft_round = Column(Integer)
    draft_number = Column(Integer)
    team_id = Column(Integer, ForeignKey('teams.id'))

    team = relationship("Team")

    def __repr__(self) -> str:
        return f"<Player {self.first_name}> {self.last_name}"

    def __str__(self) -> str:
        return self.first_name

    def __hash__(self) -> int:
        return hash(self.first_name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Player):
            return self.id == other.id
        return False

    @property
    def created(self) -> datetime:
        """Datetime weather report was created from ID"""
        return self.d.generation_time

    @classmethod
    async def by_city(cls, id: int) -> "Player":
        """Get a weather report by city"""
        return await cls.find_one({"id": id})

class GameSchema(BaseModel):
    id: int
    date: str
    season: int
    status: str
    period: int
    time: str
    postseason: bool
    home_team_score: int
    visitor_team_score: int
    home_team: TeamSchema
    visitor_team: TeamSchema

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    season = Column(Integer)
    status = Column(String)
    period = Column(Integer)
    time = Column(String)
    postseason = Column(Integer)
    home_team_score = Column(Integer)
    visitor_team_score = Column(Integer)
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    visitor_team_id = Column(Integer, ForeignKey('teams.id'))

    home_team = relationship("Team", foreign_keys=[home_team_id])
    visitor_team = relationship("Team", foreign_keys=[visitor_team_id])

    def __repr__(self) -> str:
        return f"Game({self.date}, {self.home_team.full_name} vs {self.visitor_team.full_name})"

    def __str__(self) -> str:
        return self.city

    def __hash__(self) -> int:
        return hash(self.city)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Game):
            return self.id == other.id
        return False

    @property
    def created(self) -> datetime:
        """Datetime weather report was created from ID"""
        return self.d.generation_time

    @classmethod
    async def by_city(cls, id: int) -> "Game":
        """Get a weather report by city"""
        return await cls.find_one({"id": id})

