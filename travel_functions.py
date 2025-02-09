import random

# cities_idx helper
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
    player, cities_idx
):  # input: player dictionary, cities_idx list output: player dictionary
    """Allow player to travel between cities"""
    if player["city"] == cities_idx[0]:  # feldor node
        print(f"Where would you like to go?")
        print("1. Crankston")
        print("2. Cabella")
        print("3. Foyella")
        print("4. Hardrock")
        print("5. Exit")
        choice = int(input())
        if choice == 1:
            # crankston
            player["city"] = cities_idx[1]
            print(player["city"])  # debuggin
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Crankston.")
            return player
        if choice == 2:
            # cebella
            player["city"] = cities_idx[3]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Cabella.")
            return player
        if choice == 3:
            # foyella
            player["city"] = cities_idx[4]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Foyella.")
            return player
        if choice == 4:
            # hardrock
            player["city"] = cities_idx[6]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Hardrock")
            return player
        else:
            return player

    if player["city"] == cities_idx[1]:  # crankston node
        print(f"Where would you like to go?")
        print("1. Tetra Tower")
        print("2. Feldor")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            # tetra tower
            player["city"] = cities_idx[2]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Tetra Tower.")
            return player
        if choice == 2:
            # feldor
            player["city"] = cities_idx[0]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Feldor.")
            return player
        else:
            return player

    if player["city"] == cities_idx[2]:  # Tetra Tower node
        print(f"Where would you like to go?")
        print("1. Crankston")
        print("2. Exit")
        choice = int(input())
        if choice == 1:
            # crankston
            player["city"] = cities_idx[1]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Crankston.")
            return player
        else:
            return player

    if player["city"] == cities_idx[6]:  # hardrock node
        print("1. Feldor")
        print("2. Caralo")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            # feldor
            player["city"] = cities_idx[0]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Feldor.")
            return player
        if choice == 2:
            # caralo
            player["city"] = cities_idx[5]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Caralo")
            return player
        else:
            return player

    if player["city"] == cities_idx[5]:  # caralo node
        print("1. Cebella")
        print("2. Hardrock")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            # Cebella
            player["city"] = cities_idx[3]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Cebella.")
            return player
        if choice == 2:
            # hardrock
            player["city"] = cities_idx[6]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Hardrock")
            return player
        else:
            return player

    if player["city"] == cities_idx[3]:  # Cebella node
        print("1. Foyella")
        print("2. Feldor")
        print("3. Caralo")
        print("4. Exit")
        choice = int(input())
        if choice == 1:
            # Foyella
            player["city"] = cities_idx[4]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Foyella")
            return player
        if choice == 2:
            # feldor
            player["city"] = cities_idx[0]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Feldor.")
            return player
        if choice == 3:
            # caralo
            player["city"] = cities_idx[5]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Caralo")
            return player
        else:
            return player

    if player["city"] == cities_idx[4]:  # Foyella node
        print("1. Silter")
        print("2. Feldor")
        print("3. Cebella")
        print("4. Exit")
        choice = int(input())
        if choice == 1:
            # Silter
            player["city"] = cities_idx[7]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Silter")
            return player
        if choice == 2:
            # feldor
            player["city"] = cities_idx[0]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Feldor.")
            return player
        if choice == 3:
            # Cebella
            player["city"] = cities_idx[3]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Cebella.")
            return player
        else:
            return player
    if player["city"] == cities_idx[7]:  # Silter node
        print("1. Tobunia")
        print("2. Ratherberg")
        print("3. Foyella")
        print("4. Exit")
        choice = int(input())
        if choice == 1:
            # Tobunia
            player["city"] = cities_idx[9]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Tobunia.")
            return player
        if choice == 2:
            # Ratherberg
            player["city"] = cities_idx[8]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Ratherberg.")
            return player
        if choice == 3:
            # Foyella
            player["city"] = cities_idx[4]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Foyella")
            return player
        else:
            return player
    if player["city"] == cities_idx[9]:  # Tobunia node
        print("1. Ratherberg")
        print("2. Silter")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            # Ratherberg
            player["city"] = cities_idx[8]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Ratherberg.")
            return player
        if choice == 2:
            # Silter
            player["city"] = cities_idx[7]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Silter")
            return player
        else:
            return player

    if player["city"] == cities_idx[9]:  # Ratherberg node
        print("1. Silter")
        print("2. Tobunia")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            # Silter
            player["city"] = cities_idx[7]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Silter")
            return player
        if choice == 2:
            # Tobunia
            player["city"] = cities_idx[9]
            print(random.choice(player["city"]["intro_text"]))
            print("You have arrived in Tobunia.")
            return player
        else:
            return player
    return player
