from initial_generation import (
    Feldor_Initialization,
    Crankston_Initialization,
    Tetra_Tower_Initialization,
    Cabella_Initialization,
    Foyella_Initialization,
)
import random

"""Cities Guide
Feldor -> cities[0]
Crankston -> cities[1]
"""
cities = [
    Feldor_Initialization(),
    Crankston_Initialization(),
    Tetra_Tower_Initialization(),
    Cabella_Initialization(),
    Foyella_Initialization(),
]
Feldor = cities[0]
Crankston = cities[1]
Tetra_Tower = cities[2]
Cabella = cities[3]
Foyella = cities[4]


def Map_Total_Supplies(
    product,
):  # input:  City Dictionary, Output:  total supply of chosen product for all cities
    total_supply = 0
    for city in cities:
        total_supply += city["corn"]["supply"]
    return total_supply


def Price_Calculator(
    city, product
):  # input: city dictionary, str(product), Output:  Product Dictionary w/ updated goods prices:
    total_product = Map_Total_Supplies(city[product]["supply"])
    market_cap = total_product * city[product]["base_price"]
    city[product]["moving_price"] = int(market_cap / city[product]["supply"])
    return city


def Money_Converter(
    integer,
):  # input: integer, output: string of gold, silver, and copper abbreviated as 1g, 1s, 1c
    gold = integer // 1000
    silver = (integer % 1000) // 100
    copper = integer % 100
    return f"{gold}g {silver}s {copper}c"


def spcr(width=50, pattern="="):
    print("\n" + pattern * width + "\n")
