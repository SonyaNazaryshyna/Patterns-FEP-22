from django.db import models

# Create your models here.

class TileFactory:
    @staticmethod
    def _get_entity_value(entity, key, default='N/A'):
        if isinstance(entity, dict):
            return entity.get(key, default)
        return getattr(entity, key, default)

    @staticmethod
    def create_player_tile(entity):
        return {
            'id': TileFactory._get_entity_value(entity, 'id'),
            'first_name': TileFactory._get_entity_value(entity, 'first_name'),
            'last_name': TileFactory._get_entity_value(entity, 'last_name'),
            'position': TileFactory._get_entity_value(entity, 'position'),
            'height': TileFactory._get_entity_value(entity, 'height'),
            'weight': TileFactory._get_entity_value(entity, 'weight'),
            'jersey_number': TileFactory._get_entity_value(entity, 'jersey_number'),
            'college': TileFactory._get_entity_value(entity, 'college', 'N/A'),
            'country': TileFactory._get_entity_value(entity, 'country'),
            'draft_year': TileFactory._get_entity_value(entity, 'draft_year', 'N/A'),
            'draft_round': TileFactory._get_entity_value(entity, 'draft_round', 'N/A'),
            'draft_number': TileFactory._get_entity_value(entity, 'draft_number', 'N/A'),
            'team_name': TileFactory._get_entity_value(entity, 'team_name', 'N/A'),
            'team_city': TileFactory._get_entity_value(entity, 'team_city', 'N/A')
        }

    @staticmethod
    def create_team_tile(entity):
        return {
            'id': TileFactory._get_entity_value(entity, 'id'),
            'full_name': TileFactory._get_entity_value(entity, 'full_name'),
            'city': TileFactory._get_entity_value(entity, 'city'),
            'division': TileFactory._get_entity_value(entity, 'division'),
            'conference': TileFactory._get_entity_value(entity, 'conference')
        }
