from running_functions import Money_Converter, Price_Calculator


def market_interact(market, wagon, item, amount):  # TIED TO visit_market()
    # Calculate total wagon money in copper pieces
    total_copper = (
        wagon["cart"]["gold"] * 1000
        + wagon["cart"]["silver"] * 100
        + wagon["cart"]["copper"]
    )

    if amount > 0:  # Buying
        # Check if market has enough supply
        if amount > market[item]["supply"]:
            print(f"The market doesn't have enough {item} in stock")
            return wagon

        cost = market[item]["moving_price"] * amount
        cost_str = Money_Converter(cost)  # For display purposes

        if cost <= total_copper:
            # Convert total transaction cost to currency denominations
            remaining_copper = total_copper - cost
            wagon["cart"]["gold"] = remaining_copper // 1000
            wagon["cart"]["silver"] = (remaining_copper % 1000) // 100
            wagon["cart"]["copper"] = remaining_copper % 100

            market[item]["supply"] -= amount
            print(f"You bought {amount} {item} for {cost_str}")
        else:
            print(f"You don't have enough money. Cost is {cost_str}")

    elif amount < 0:  # Selling
        sell_amount = abs(amount)
        profit = market[item]["moving_price"] * sell_amount
        profit_str = Money_Converter(profit)  # For display purposes

        # Add profit to wagon's money
        new_total = total_copper + profit
        wagon["cart"]["gold"] = new_total // 1000
        wagon["cart"]["silver"] = (new_total % 1000) // 100
        wagon["cart"]["copper"] = new_total % 100

        market[item]["supply"] += sell_amount
        print(f"You sold {sell_amount} {item} for {profit_str}")

    else:  # amount == 0
        print("Please enter a non-zero amount")

    return wagon


def visit_market(
    wagon, city
):  # input: wagon dictionary, city dictionary, Output: wagon dictionary
    while True:
        market = city
        corn_price = Price_Calculator(market, "corn")
        print("1.  Corn: " + Money_Converter(market["corn"]["moving_price"]))
        iron_ore_price = Price_Calculator(market, "iron_ore")
        print("2.  Iron Ore: " + Money_Converter(market["iron_ore"]["moving_price"]))
        print("3.  Go back")
        action = input()

        if action == "1":  # for corn
            print("Amount to trade?")
            item = "corn"
            amount = int(input())
            market_interact(market, wagon, item, amount)

        elif action == "2":  # for iron ore
            print("Amount to trade?")
            item = "iron_ore"
            amount = int(input())
            market_interact(market, wagon, item, amount)

        elif action == "3":
            break
