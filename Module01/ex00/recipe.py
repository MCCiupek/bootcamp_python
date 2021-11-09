import sys

class Recipe:
    """Recipe class"""
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=None):
        """Object Instantiation"""
        try:
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = [str(i) for i in ingredients]
            self.recipe_type = str(recipe_type)
            self.description = str(description)
            self.__check_values__()
        except ValueError as err:
            sys.stderr.write("Error: Instantiation of object Recipe failed: {0}\n".format(err))
            sys.exit()
    
    def __check_values__(self):
        """Check attributes values"""
        if self.cooking_lvl not in range(1, 5):
            raise ValueError("Cooking level must be in range 1 to 5.")
        if self.cooking_time < 0:
            raise ValueError("Cooking time must be a positive integer.")
        if self.recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("Recipe type must be either  \"starter\", \"lunch\" or \"dessert\".")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "-- {0} --\nDifficulty: {1}/5\n\
                    \rCooking Time: {2}min\n\
                    \rIngredients: {3}\n\
                    \rType: {4}\n\
                    \rDescription: {5}\n\
                    \r---{6}---".format(self.name,
                                                 self.cooking_lvl,
                                                 self.cooking_time,
                                                 self.ingredients,
                                                 self.recipe_type,
                                                 self.description,
                                                 "-" * len(self.name))
        return txt