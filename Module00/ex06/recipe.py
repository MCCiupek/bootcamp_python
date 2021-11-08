import sys

cookbook = {'sandwich': {'ingredients':
                         ['ham', 'bread', 'cheese', 'tomatoes'],
                         'meal': 'lunch', 'prep_time': 10},
            'cake': {'ingredients': ['flour', 'sugar', 'eggs'],
                     'meal': 'dessert', 'prep_time': 60},
            'salad': {'ingredients':
                      ['avocado', 'arugula', 'tomatoes', 'spinach'],
                      'meal': 'lunch', 'prep_time': 15}}


select_opt = "Please select an option by typing the corresponding number:\n\
1: Add a recipe\n\
2: Delete a recipe\n\
3: Print a recipe\n\
4: Print the cookbook\n\
5: Quit\n"

unknown_opt = "This option does not exist, \
please type the corresponding number. \
To exit, enter 5.\n"

# print(cookbook.keys())
# print(cookbook.values())
# print(cookbook.items())


def print_recipe(name):
    print("\nRecipe for {0}".format(name))
    print("Ingredients list: {0}".format(cookbook[name]['ingredients']))
    print("To be eaten for {0}".format(cookbook[name]['meal']))
    print("Takes {0} minutes of cooking".format(cookbook[name]['prep_time']))


def delete_recipe(name):
    del cookbook[name]


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {'ingredients': ingredients,
                      'meal': meal,
                      'prep_time': prep_time}


def print_cookbook():
    print("--- COOKBOOK ---")
    for recipe in cookbook:
        print_recipe(recipe)
    print("----------------")


def quit_cookbook():
    sys.exit("Cookbook closed.")


def add_recipe_input():
    name = input("Recipe's name: ")
    ingredients = input("Ingredients (comma-separated): ")
    meal = input("Meal: ")
    prep_time = input("Prep time (in min): ")
    try:
        add_recipe(name, ingredients.split(','), meal, int(prep_time))
    except ValueError:
        print("Error: couldn't add recipe.")


def print_recipe_input():
    name = input("Please enter the recipe's name to get its details: ")
    try:
        print_recipe(name)
    except KeyError:
        print("Error: Recipe not found.")


def delete_recipe_input():
    name = input("Please enter the recipe's name: ")
    try:
        delete_recipe(name)
    except KeyError:
        print("Error: Recipe not found.")


options = {
           1: add_recipe_input,
           2: delete_recipe_input,
           3: print_recipe_input,
           4: print_cookbook,
           5: quit_cookbook,
}

n = input(select_opt)
while (42):
    try:
        opt = int(n)
        options[opt]()
        n = input(select_opt)
    except ValueError:
        n = input(unknown_opt)
    except KeyError:
        n = input(unknown_opt)
