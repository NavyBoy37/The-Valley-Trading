def Map_Total_Supplies(
    product, cities_idx
):  # input:  City Dictionary, Output:  total supply of chosen product for all cities
    total_supply = 0
    for city in cities_idx:
        total_supply += city["corn"]["supply"]
    return total_supply


def Price_Calculator(
    city, product, cities_idx
):  # input: city dictionary, str(product), Output:  Product Dictionary w/ updated goods prices:
    """
    The way good prices are calculated is by adding the product supplies across all the cities,
    multiplying them by a "base price" that is set in initial_generation for each city,
    and dividing that market cap by each city's individual supply.
    Dependencies:
    -Map_Total_Supplies() in running_functions.py
    """
    total_product = Map_Total_Supplies(city[product]["supply"], cities_idx)
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


def display_coins(coins):  # TIED TO market_interact()
    """Display exactly what coins are in possession"""
    return f"{coins['gold']}g {coins['silver']}s {coins['copper']}c"


def spcr(width=50, pattern="="):
    """
    For UI purposes.  Separates user actions in terminal
    """
    print("\n" + pattern * width + "\n")


def calculate_total_weight(cart):
    """Calculate current cart weight"""
    from initial_generation import ITEM_WEIGHTS  # Import at top of file

    total_weight = 0
    for item, amount in cart.items():
        if item in ITEM_WEIGHTS:  # Check in case of non-weighted items
            total_weight += ITEM_WEIGHTS[item] * amount
    return total_weight
