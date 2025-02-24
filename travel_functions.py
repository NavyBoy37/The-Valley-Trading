import random
from running_functions import spcr

"""
cities_idx helper
These numbers are positions in the cities_idx list
where game data is stored during run time.  initial_generation.py
generates city dictionaries into that list in main.py
"""
# 0 Feldor
# 1 Crankston
# 2 Tetra Tower
# 3 Cabella
# 4 Foyella
# 5 Caralo
# 6 Hardrock
# 7 Silter
# 8 Ratherberg
# 9 Tobunia


def travel(
    player, cities_idx, wagon
):  # input: player dictionary, cities_idx, wagon list output: player dictionary, wagon
    """
    travel() uses if then statements to build the world map, along with changing
    the city dictionary in the player dictionary to change location.  Only certain cities
    are accessible from others.  Adding new cities is tedious right now.  Adding more
    here requires new initial_generation functions and adding to cities_idx list in main.py
    for initialization
    """
    # Store the starting location before changing it
    start_location = player["city"]["name"]

    if player["city"] == cities_idx[0]:  # feldor node
        print(f"Where would you like to go?")
        print("1. Crankston")
        print("2. Cabella")
        print("3. Foyella")
        print("4. Hardrock")
        print("5. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # crankston
            player["city"] = cities_idx[1]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Crankston.")
            return player, wagon
        if choice == 2:
            # cebella
            player["city"] = cities_idx[3]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Cabella.")
            return player, wagon
        if choice == 3:
            # foyella
            player["city"] = cities_idx[4]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Foyella.")
            return player, wagon
        if choice == 4:
            # hardrock
            player["city"] = cities_idx[6]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Hardrock")
            return player, wagon
        else:
            return player, wagon

    if player["city"] == cities_idx[1]:  # crankston node
        print(f"Where would you like to go?")
        print("1. Tetra Tower")
        print("2. Feldor")
        print("3. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # tetra tower
            player["city"] = cities_idx[2]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Tetra Tower.")
            return player, wagon
        if choice == 2:
            # feldor
            player["city"] = cities_idx[0]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Feldor.")
            return player, wagon
        else:
            return player, wagon

    if player["city"] == cities_idx[2]:  # Tetra Tower node
        print(f"Where would you like to go?")
        print("1. Crankston")
        print("2. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # crankston
            player["city"] = cities_idx[1]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Crankston.")
            return player, wagon
        else:
            return player, wagon

    if player["city"] == cities_idx[6]:  # hardrock node
        print("1. Feldor")
        print("2. Caralo")
        print("3. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # feldor
            player["city"] = cities_idx[0]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Feldor.")
            return player, wagon
        if choice == 2:
            # caralo
            player["city"] = cities_idx[5]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Caralo")
            return player, wagon
        else:
            return player, wagon

    if player["city"] == cities_idx[5]:  # caralo node
        print("1. Cebella")
        print("2. Hardrock")
        print("3. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # Cebella
            player["city"] = cities_idx[3]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Cebella.")
            return player, wagon
        if choice == 2:
            # hardrock
            player["city"] = cities_idx[6]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Hardrock")
            return player, wagon
        else:
            return player, wagon

    if player["city"] == cities_idx[3]:  # Cebella node
        print("1. Foyella")
        print("2. Feldor")
        print("3. Caralo")
        print("4. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # Foyella
            player["city"] = cities_idx[4]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Foyella")
            return player, wagon
        if choice == 2:
            # feldor
            player["city"] = cities_idx[0]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Feldor.")
            return player, wagon
        if choice == 3:
            # caralo
            player["city"] = cities_idx[5]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Caralo")
            return player, wagon
        else:
            return player, wagon

    if player["city"] == cities_idx[4]:  # Foyella node
        print("1. Silter")
        print("2. Feldor")
        print("3. Cebella")
        print("4. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # Silter
            player["city"] = cities_idx[7]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Silter")
            return player, wagon
        if choice == 2:
            # feldor
            player["city"] = cities_idx[0]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Feldor.")
            return player, wagon
        if choice == 3:
            # Cebella
            player["city"] = cities_idx[3]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Cebella.")
            return player, wagon
        else:
            return player, wagon

    if player["city"] == cities_idx[7]:  # Silter node
        print("1. Tobunia")
        print("2. Ratherberg")
        print("3. Foyella")
        print("4. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # Tobunia
            player["city"] = cities_idx[9]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Tobunia.")
            return player, wagon
        if choice == 2:
            # Ratherberg
            player["city"] = cities_idx[8]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Ratherberg.")
            return player, wagon
        if choice == 3:
            # Foyella
            player["city"] = cities_idx[4]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Foyella")
            return player, wagon
        else:
            return player, wagon

    if player["city"] == cities_idx[9]:  # Tobunia node
        print("1. Ratherberg")
        print("2. Silter")
        print("3. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # Ratherberg
            player["city"] = cities_idx[8]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Ratherberg.")
            return player, wagon
        if choice == 2:
            # Silter
            player["city"] = cities_idx[7]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Silter")
            return player, wagon
        else:
            return player, wagon

    if player["city"] == cities_idx[8]:  # Ratherberg node (fixed the comment)
        print("1. Silter")
        print("2. Tobunia")
        print("3. Exit")
        choice = int(input())
        spcr()
        if choice == 1:
            # Silter
            player["city"] = cities_idx[7]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Silter")
            return player, wagon
        if choice == 2:
            # Tobunia
            player["city"] = cities_idx[9]
            wagon = supply_cost(player, start_location, wagon)
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Tobunia.")
            return player, wagon
        else:
            return player, wagon


def supply_cost(player, start_location, wagon):
    """
    Dependency of travel().  Calculates supplies used during travel which determines distance.  Also has failure condition from starvation.
    """
    from initial_generation import ROAD_LENGTHS
    import sys

    # Construct the road key correctly
    road_key = "Road_" + start_location + "_" + player["city"]["name"]

    # Check if the road key exists in ROAD_LENGTHS
    if road_key in ROAD_LENGTHS:
        length = ROAD_LENGTHS[road_key]
        # Deduct supplies based on road length
        wagon["cart"]["supplies"] = wagon["cart"]["supplies"] - length
        if wagon["cart"]["supplies"] < 0:
            print("You ran out of supplies on the road. You have died")
            print(
                """
                +------------------+
                |    GAME OVER     |
                +------------------+
                """
            )
            sys.exit()
    else:
        print(
            f"Warning: No road found between {start_location} and {player['city']['name']}"
        )

    return wagon
