"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
from Food import Food

def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    # Your code here
    food_name=str(input("Name: "))
    print(Food.origins())
    food_origin=int(input("Select origin (0-11): "))
    food_vegetarian=bool(input("Vegetarian (True/False): "))
    print(food_vegetarian)
    food_calories=int(input("Calories: "))
    print(food_calories)
    
    food=Food(food_name, food_origin, food_vegetarian, food_calories)
    
    return food

#task 4
def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    

    data=line.strip().split("|")
    
    name=str(data[0])
    origin=int(data[1])
    
    if data[2]=="False":
        vegetarian=False
    elif data[2]=="True":
        vegetarian=True
    calories=int(data[3])
    food=Food(name, origin, vegetarian, calories)
    
    return food



def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    
    foods=[]
    line=file_variable.readline()

    while line!="":
        foods_item=line.split("|")
        name, origin, is_vegetarian, calories = (foods_item[0], int(foods_item[1]), foods_item[2]=="True", int(foods_item[3]))
        
        food_object=Food(name, origin, is_vegetarian, calories)
        foods.append(food_object)
        line=file_variable.readline()
    
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    for food in foods:
        food.write(file_variable)
    return None
  

    


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies=[]
    
    for food in foods:
        if food.is_vegetarian:
            veggies.append(food)
    
    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins=[]
    for food in foods:
        if food.origin==origin:
            origins.append(food)
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    total_calories=0
    for food in foods:
        total_calories+=food.calories
    
    avg=total_calories/len(foods)
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    total_calories=0
    origin_count=0
    
    
    for food in foods:
        if food.origin==origin:
            total_calories+=food.calories
            origin_count+=1
    if origin_count !=0 :
        avg=total_calories/origin_count
    else:
        avg=0
        
    
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    foods_sorted=sorted(foods, key=lambda food:food.name)
    ORIGINS=Food.origins()
    print('{:<35} {:<15} {:>10} {:>8}'.format("Food", "Origin", "Vegetarian", "Calories"))
    print('{:<35} {:<15} {:>10} {:>8}'.format("-----------------------------------", "---------------", "----------", "--------"))
    for food in foods_sorted:
        origin_name=ORIGINS[food.origin]
        print('{:<35} {:<15} {:>10} {:>8}'.format(food.name, origin_name, str(food.is_vegetarian), food.calories))


    return

def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result=[]
    for food in foods:
        if origin==-1 or food.origin==origin and max_cals==0 or food.calories<=max_cals and is_veg is False or food.is_vegetarian==is_veg:
            result.append(food)
            

    return result
