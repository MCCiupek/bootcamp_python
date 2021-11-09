import sys
from recipe import Recipe
from book import Book

tourte = Recipe("Tourte", 2, 60, ["chicken", "mushrooms", "pastry"], "lunch")
print(tourte.__str__())

tourte_vg = Recipe("Veggie Tourte", 2, 50,
                   ["carrots", "leaks", "mushrooms", "pastry"],
                   "lunch", "Delicious warm veggie lunch")
print(tourte_vg.__str__())

cookbook = Book("My Cookbook")
cookbook.add_recipe(tourte)

types = ["starter", "lunch", "dessert", 123]

for t in types:
    try:
        recipies = "{0}: {1}".format(t, cookbook.get_recipes_by_types(t))
        print(recipies)
    except ValueError:
        pass
    except KeyError:
        pass

try:
    print(cookbook.get_recipe_by_name("Tourte"))
    print(cookbook.get_recipe_by_name("Veggie Tourte"))
except KeyError:
    pass
