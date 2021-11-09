import sys
from datetime import datetime
from recipe import Recipe

INIT_FAILED = "Error: Instantiation of object Recipe failed: {0}\n"
UNK_RCP = "The recipe of {0} is not in cookbook {1}"
UNK_TYP =
class Book:
    """Book class"""
    def __init__(self, name):
        """Object Instantiation"""
        try:
            self.name = str(name)
            self.last_update = datetime.now()
            self.creation_time = datetime.now()
            self.recipe_list = {"starter": [], "lunch": [], "dessert": []}
        except ValueError as err:
            sys.stderr.write(INIT_FAILED.format(err))
            sys.exit()

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for key in self.recipe_list.keys():
            if name in self.get_recipes_by_types(key):
                for recipe in self.recipe_list[key]:
                    if recipe.name == name:
                        print(recipe.__str__())
                        return recipe
        sys.stderr.write(UKN_RCP.format(name, self.name))
        raise KeyError

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in self.recipe_list.keys():
            sys.stderr.write("Unknowned recipe type: {0}\n".format(recipe_type))
            raise KeyError
        return [r.name for r in self.recipe_list[recipe_type]]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("Object {0} is not a recipe.".format(type(recipe)))
        else:
            self.last_update = datetime.now()
            self.recipe_list[recipe.recipe_type].append(recipe)
