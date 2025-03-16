"""TODO:  Add first story point/quest line"""

"""TODO:  Use above days-to-travel system to calculate new moving prices for products"""
"""TODO:  """
"""TODO:  add credit system so you can over extend and risk it for the biscuit"""

"""NOTE ON BALANCING.  VERY HEAVY ITEMS SHOULD BE EXPENSIVE, HEAVY, AND FLUCTUATE WILDLY.  Cheap items should be stable and not move much.
At the very least Heavy = high variance and light = low variance.  If light has high variance it must be expensive as hell.
"""
import sys
from travel_functions import travel
from running_functions import spcr
from market_functions import visit_market
from exchange_functions import visit_money_exchange
from save_game import save_game, load_game, list_save_files
from initial_generation import (
    Feldor_Initialization,
    Crankston_Initialization,
    Tetra_Tower_Initialization,
    Cabella_Initialization,
    Foyella_Initialization,
    Hardrock_Initialization,
    Caralo_Initialization,
    Silter_Initialization,
    Ratherberg_Initialization,
    Tobunia_Initialization,
    Wagon_Initialization,
    Player_Initialization,
)


cities_idx = [  # this exists to pass through each game function so that data gets updated and carried forward
    Feldor_Initialization(),  # 0
    Crankston_Initialization(),  # 1
    Tetra_Tower_Initialization(),  # 2
    Cabella_Initialization(),  # 3
    Foyella_Initialization(),  # 4
    Caralo_Initialization(),  # 5
    Hardrock_Initialization(),  # 6
    Silter_Initialization(),  # 7
    Ratherberg_Initialization(),  # 8
    Tobunia_Initialization(),  # 9
]


while True:
    spcr()
    print("Main Menu")
    print("1. Load Game")
    print("2. New Game")
    print("3. Exit Game")
    choice = str(input())
    spcr()

    if choice == "1":
        list_save_files("save")
        print("Please enter file name")
        file_name = str(input())
        player, wagon, cities_idx = load_game(file_name)
        break

    if choice == "2":
        player = Player_Initialization()
        wagon = Wagon_Initialization()
        player["city"] = cities_idx[0]
        break

    if choice == "3":
        sys.exit()

# Game Intro Section
print(
    "You finally did it... After years of hard work, you have enough silver to buy a cart."
)
print(". . .")
print(
    "It's not much, but it's got wheels.  With "
    + str(wagon["cart"]["silver"])
    + " silver, you can finally start your journey.  You set your sights on the horizon."
)

# Main Loop Section
while True:

    print("Location:  " + player["city"]["name"])
    print("1. Travel")
    print("2. Visit Market")
    print("3. Visit Money Exchange")
    print("8. Save Game")
    print("9. Quit Game")
    choice = str(input())

    if choice == "1":
        spcr()
        player, wagon = travel(player, cities_idx, wagon)
    if choice == "2":
        spcr()
        wagon, cities_idx = visit_market(wagon, player["city"], cities_idx)
    if choice == "3":
        spcr()
        wagon = visit_money_exchange(wagon, player["city"])
    if choice == "8":
        print("Input file name...")
        file_name = str(input())
        save_game(player, wagon, cities_idx, file_name)
        print("Game Saved")
        spcr()
    if choice == "9":
        sys.exit()
