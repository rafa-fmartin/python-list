from typing import List, Dict


def recipe(ingredients: List[str], meal: str, prep_time: int) -> Dict:
    return {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time,
    }


def get_recipe_names(cookbook: Dict):
    for recipe_name in cookbook.keys():
        print(recipe_name)


def get_recipe(cookbook: Dict, recipe_name: str):
    if recipe_name in cookbook.keys():
        print(
            """\nRecipe for {name}
    Ingredients list: {ingredients}
    To be eaten for {meal}
    Takes {prep_time} minutes of cooking
""".format(
                name=recipe_name,
                ingredients=cookbook.get(recipe_name).get("ingredients"),
                meal=cookbook.get(recipe_name).get("meal"),
                prep_time=cookbook.get(recipe_name).get("prep_time"),
            ),
            end="",
        )
        return
    print("\nRecipe does not exist in the cookbook.")


def delete_recipe(cookbook: Dict, recipe_name: str):
    if recipe_name in cookbook.keys():
        cookbook.pop(recipe_name, None)
        return
    print("\nRecipe does not exist in the cookbook.")


def add_recipe(cookbook: Dict):
    print("\nEnter a name: ")
    recipe_name = input()
    ingredients = []
    print("Enter ingredients:")
    while True:
        ingredient = input()
        if ingredient == "":
            break
        ingredients.append(ingredient)
    print("Enter meal: ")
    meal = input()
    print("Enter preparation time: ", end="\n")
    prep_time = input()

    cookbook[recipe_name] = recipe(ingredients, meal, prep_time)


def available_options():
    print(
        "List of available option:\n"
        "   1: Add a recipe\n"
        "   2: Delete a recipe\n"
        "   3: Print a recipe\n"
        "   4: Print the cookbook\n"
        "   5: Quit"
    )


def menu(cookbook: Dict):
    option = 0
    print("Welcome to the Python Cookbook!")
    available_options()
    while option != 5 or not option.isdigit():
        print("\nPlease select an option:")
        option = input()
        option = int(option) if option.isdigit() else 0
        if option == 1:
            add_recipe(cookbook)
        elif option == 2:
            print("\nEnter the recipe's name to delete: ")
            recipe_name = input()
            delete_recipe(cookbook, recipe_name)
        elif option == 3:
            print("\nPlease enter a recipe name to get its details:")
            recipe_name = input()
            get_recipe(cookbook, recipe_name)
        elif option == 4:
            get_recipe_names(cookbook)
        elif option == 5:
            print("\nCookbook closed. Goodbye !")
            return
        else:
            print("\nSorry, this option does not exist.")
            available_options()


def main():
    cookbook = {
        "sandwich": recipe(["ham", "bread", "cheese", "tomatoes"], "lunch", 10),
        "cake": recipe(["flour", "sugar", "eggs"], "dessert", 60),
        "salad": recipe(["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15),
    }
    menu(cookbook)


if __name__ == "__main__":
    main()
