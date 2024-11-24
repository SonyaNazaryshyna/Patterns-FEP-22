from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.coercions import expect
from sqlalchemy.sql.sqltypes import NULLTYPE

from backend.db.database import DBConnection
from backend.models.api_models import Player, Team, TeamSchema, PlayerSchema


def add_player_to_db(player_data):
    """
    Adds a player record to the database.

    Args:
        player_data (dict): Dictionary containing player details.
    Returns:
        str: Success or error message.
    """
    try:
        db = DBConnection()
        db.connect()

        existing_player = db.sessio.query(Player).filter_by(id=player_data['id']).first()

        if existing_player:
            return "Player already exists"
        print(
            f"draft_year: {player_data['draft_year']}, draft_round: {player_data['draft_round']}, draft_number: {player_data['draft_number']}, team_id: {player_data['team_id']}")

        new_player = Player(
            id=player_data['id'],
            first_name=player_data['first_name'],
            last_name=player_data['last_name'],
            position=player_data['position'],
            height=player_data['height'],
            weight=player_data['weight'],
            jersey_number=player_data['jersey_number'],
            college=player_data['college'],
            country=player_data['country'],draft_year = player_data['draft_year'] if isinstance(player_data['draft_year'], int) else 0,
            draft_round = player_data['draft_round'] if isinstance(player_data['draft_round'], int) else 0,
            draft_number = player_data['draft_number'] if isinstance(player_data['draft_number'], int) else 0,
            team_id = player_data['team_id'] if isinstance(player_data['team_id'], int) else 0
        )

        db.sessio.add(new_player)
        db.sessio.commit()

        return "Player added successfully"

    except Exception as e:
        return f"Error adding player: {str(e)}"

    finally:
        db.disconnect()

def add_team_to_db(team_data):
    try:
        db = DBConnection()
        db.connect()

        existing_team = db.sessio.query(Team).filter_by(id=team_data['id']).first()
        if existing_team:
            return "Team already exists"

        team = Team(
            id=team_data['id'],
            full_name=team_data['name'],
            city=team_data['city'],
            division=team_data['division'],
            conference=team_data['conference']
        )

        db.sessio.add(team)
        db.sessio.commit()
        return "Team added successfully"

    except Exception as e:
        return f"Error adding team: {str(e)}"

async def read_teams():
    try:
        db = DBConnection()
        db.connect()
        teams = db.sessio.query(Team).all()

        team_list = [TeamSchema.from_orm(team) for team in teams]
        return team_list

    except Exception as e:
        print(f"Error fetching teams: {e}")
        return []

def read_players():
    try:
        db = DBConnection()
        db.connect()
        players = db.sessio.query(Player).all()

        players_list = [PlayerSchema.from_orm(player) for player in players]
        return players_list

    except Exception as e:
        return f"Error fetching team: {str(e)}"

def delete_team_from_db(team_id):
    try:
        db = DBConnection()
        db.connect()
        print(f"Delete {team_id}")
        db.sessio.query(Team).filter_by(id=team_id).delete()
        db.sessio.commit()
        return "Team deleted successfully"
    except Exception as e:
        return f"Error deleting team: {str(e)}"

def delete_player_from_db(player_id):
    try:
        db = DBConnection()
        db.connect()
        print(f"Delete {player_id}")
        db.sessio.query(Player).filter_by(id=player_id).delete()
        db.sessio.commit()
        return "Player deleted successfully"
    except Exception as e:
        return f"Error deleting player: {str(e)}"




















