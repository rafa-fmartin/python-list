from typing import List


class Recipe:
    def __init__(
        self,
        name: str,
        cooking_lvl: int,
        cooking_time: int,
        ingredients: List,
        recipe_type: str,
        description: str = "",
    ):
        self.name = name
        if cooking_lvl in range(1, 6):
            self.cooking_lvl = cooking_lvl
        else:
            print("cooking_lvl")
            return
        if cooking_time >= 0:
            self.cooking_time = cooking_time
        else:
            print("cooking_time")
            return
        self.ingredients = ingredients
        if recipe_type not in ["starter", "lunch", "dessert"]:
            self.recipe_type = recipe_type
        else:
            print("")
            return
        self.description = description

    def __str__(self):
        txt = """Recipe: {}
    Cooking level: {}
    Cooking time: {} minutes
    Ingredients: {}
    Description: {}
    Recipe type: {}""".format(
            self.name,
            self.cooking_lvl,
            self.cooking_time,
            ", ".join(self.ingredients)[:-2],
            self.description,
            self.recipe_type,
        )
        return txt
