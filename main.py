""" TODO:  Add lists to each city dictionary for texts to be shown to the player as they enter for the first time.  
Pull a random one from the list each time they enter the city.  This will be the city's "flavor text.  Specific unique events can come later"""

"""TODO:   Expand main.py to include a loop that allows the player to visit different cities and interact with the market.
"""
from travel_functions import travel
from running_functions import spcr
import time
from market_functions import visit_market, visit_money_exchange
from initial_generation import (
    Feldor_Initialization,
    Crankston_Initialization,
    Tetra_Tower_Initialization,
    Cabella_Initialization,
    Foyella_Initialization,
    Wagon_Initialization,
    Player_Initialization,
)


cities_idx = [  # this exists to pass through each game function so that data gets updated and carried forward
    Feldor_Initialization(),
    Crankston_Initialization(),
    Tetra_Tower_Initialization(),
    Cabella_Initialization(),
    Foyella_Initialization(),
]


"""Goods Guide
corn
iron_ore

"""
player = Player_Initialization()
wagon = Wagon_Initialization()
player["city"] = Feldor_Initialization()  # temp
# Game Intro Section
print(
    "You finally did it... After years of hard work, you have enough silver to buy a cart."
)
time.sleep(2)
print(". . .")
print(
    "It's not much, but it's got wheels.  With "
    + str(wagon["cart"]["silver"])
    + " silver, you can finally start your journey.  You set your sights on the horizon."
)

# Main Loop Section
while True:
    spcr()
    print("You are currently in " + player["city"]["name"])
    print("1. Travel")
    print("2. Visit Market")
    print("9.  Quit Game")
    choice = str(input())
    if choice == "1":
        player = travel(player, cities_idx)
    if choice == "2":
        wagon, cities_idx = visit_market(wagon, player["city"], cities_idx)
    if choice == "9":
        break
