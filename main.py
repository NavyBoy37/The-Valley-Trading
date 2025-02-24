"""TODO:  Add additional products to trade"""

"""TODO:  Add first story point/quest line"""
"""TODO:  Add food requirements for player and days/travel system for measurement of distances between cities."""
"""TODO:  Use above days-to-travel system to calculate new moving prices for products"""
"""TODO:  """
"""TODO:  Verify gems have actual weight in the cart"""
import sys
from travel_functions import travel
from running_functions import spcr
from market_functions import visit_market
from exchange_functions import visit_money_exchange
from initial_generation import (
    ITEM_WEIGHTS,
    ROAD_LENGTHS,
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


"""Goods Guide
corn
iron_ore

"""
player = Player_Initialization()
wagon = Wagon_Initialization()
player["city"] = cities_idx[0]  # temp
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
    print("9.  Quit Game")
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
    if choice == "9":
        sys.exit()
