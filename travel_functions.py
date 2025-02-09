def travel(
    player, cities_idx
):  # input: player dictionary, cities_idx list output: player dictionary
    """Allow player to travel between cities"""
    print(f"Where would you like to go?")
    print("1. Feldor")
    print("2. Crankston")
    print("3. Tetra Tower")
    print("4. Cabella")
    print("5. Foyella")
    print("6. Exit")
    choice = input()
    if choice == "1":
        player["city"] = cities_idx[0]
        print("You have arrived in Feldor.")
    elif choice == "2":
        player["city"] = cities_idx[1]
        print("You have arrived in Crankston.")
    elif choice == "3":
        player["city"] = cities_idx[2]
        print("You have arrived in Tetra Tower.")
    elif choice == "4":
        player["city"] = cities_idx[3]
        print("You have arrived in Cabella.")
    elif choice == "5":
        player["city"] = cities_idx[4]
        print("You have arrived in Foyella.")
    elif choice == "6":
        print("You decide to stay put.")
    return player
