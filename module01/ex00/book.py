from datetime import datetime
from typing import Dict
from recipe import Recipe


class Book():
    def __init__(
        self,
        name: str,
        last_update: datetime,
        creation_date: datetime,
        recipes_list: Dict[str, Recipe]
    ):
        pass
    
    def __str__(self):
        pass
    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        pass
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        pass
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
