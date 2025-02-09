from running_functions import Money_Converter, Price_Calculator, spcr


def display_coins(coins):  # TIED TO market_interact()
    """Display exactly what coins are in possession"""
    return f"{coins['gold']}g {coins['silver']}s {coins['copper']}c"


def market_interact(market, wagon, item, amount, cities_idx):
    if amount == 0:
        print("Please enter a non-zero amount")
        return wagon, cities_idx

    cart = wagon["cart"]

    # Get city index for updating
    city_index = next(
        i for i, city in enumerate(cities_idx) if city["name"] == market["name"]
    )

    if amount > 0:  # Buying
        if amount > market[item]["supply"]:
            print(f"The market doesn't have enough {item} in stock")
            return wagon, cities_idx

        unit_price = {
            "gold": market[item]["moving_price"] // 1000,
            "silver": (market[item]["moving_price"] % 1000) // 100,
            "copper": market[item]["moving_price"] % 100,
        }
        spcr()
        print(f"Cost per unit: {display_coins(unit_price)}")
        print(f"Current funds: {display_coins(cart)}")
        print("Choose payment method:")
        print("1. Gold pieces")
        print("2. Silver pieces")
        print("3. Copper pieces")
        print("4. Cancel transaction")

        choice = input()

        if choice == "4":
            return wagon, cities_idx

        denomination = {"1": "gold", "2": "silver", "3": "copper"}[choice]
        spcr()
        result_coins, success = pay_with_denomination(
            unit_price, cart, denomination, amount
        )
        if not success:
            print(f"Insufficient {denomination} pieces")
            return wagon, cities_idx

        cart = result_coins
        market[item]["supply"] -= amount
        cities_idx[city_index][item]["supply"] -= amount
        cart[item] += amount  # Add this line
        print(f"You bought {amount} {item}")

    elif amount < 0:  # Selling
        sell_amount = abs(amount)
        if cart[item] < sell_amount:  # Add this check
            print(f"You don't have enough {item} to sell")
            return wagon, cities_idx

        profit = {"copper": market[item]["moving_price"] * sell_amount}
        cart["copper"] += profit["copper"]
        cart[item] -= sell_amount  # Add this line
        market[item]["supply"] += sell_amount
        cities_idx[city_index][item]["supply"] += sell_amount
        print(f"You sold {sell_amount} {item} for {profit['copper']} copper pieces")

    wagon["cart"] = cart
    return wagon, cities_idx


def visit_money_exchange(wagon, city):
    """Allow player to convert between coin denominations with city-specific fees"""
    exchange_fees = city["exchange_fees"]

    while True:
        print(f"\nMoney Exchange - {city['name']}")
        print(f"Current funds: {display_coins(wagon['cart'])}")
        print(f"1. Convert 100 copper to 1 silver - Fee: {exchange_fees['cs']}c")
        print(f"2. Convert 10 silver to 1 gold - Fee: {exchange_fees['sg']}s")
        print(f"3. Break 1 gold to 10 silver - Fee: {exchange_fees['gs']}s")
        print(f"4. Break 1 silver to 100 copper - Fee: {exchange_fees['sc']}c")
        print("5. Exit")

        choice = input()

        if choice == "1" and wagon["cart"]["copper"] >= (100 + exchange_fees["cs"]):
            spcr()
            wagon["cart"]["copper"] -= 100 + exchange_fees["cs"]
            wagon["cart"]["silver"] += 1
            print(
                f"Converted 100 copper to 1 silver. Paid {exchange_fees['cs']} copper fee."
            )

        elif choice == "2" and wagon["cart"]["silver"] >= (10 + exchange_fees["sg"]):
            spcr()
            wagon["cart"]["silver"] -= 10 + exchange_fees["sg"]
            wagon["cart"]["gold"] += 1
            print(
                f"Converted 10 silver to 1 gold. Paid {exchange_fees['sg']} silver fee."
            )

        elif choice == "3" and wagon["cart"]["gold"] >= 1:
            spcr()
            if wagon["cart"]["silver"] >= exchange_fees["gs"]:
                wagon["cart"]["gold"] -= 1
                wagon["cart"]["silver"] += 10 - exchange_fees["gs"]
                print(
                    f"Converted 1 gold to {10 - exchange_fees['gs']} silver. Paid {exchange_fees['gs']} silver fee."
                )
            else:
                print(
                    f"Insufficient silver to pay the {exchange_fees['gs']} silver fee."
                )

        elif choice == "4" and wagon["cart"]["silver"] >= 1:
            spcr()
            wagon["cart"]["silver"] -= 1
            wagon["cart"]["copper"] += 100 - exchange_fees["sc"]
            print(
                f"Converted 1 silver to {100 - exchange_fees['sc']} copper. Paid {exchange_fees['sc']} copper fee."
            )

        elif choice == "5":
            break
        else:
            spcr()
            print("Invalid choice or insufficient coins")

    return wagon


def give_change(coins, change_amount):  # TIED TO market_interact()
    """Add change to coins without auto-converting"""
    coins["copper"] += change_amount
    return coins


def calculate_total_in_copper(coins):  # TIED TO market_interact()
    """Calculate total value in copper pieces without modifying original coin amounts"""
    return coins["gold"] * 1000 + coins["silver"] * 100 + coins["copper"]


def can_afford_with_denomination(
    cost, coins, denomination
):  # TIED TO market_interact()
    """Check if cost can be paid using a specific denomination"""
    if denomination == "gold":
        return coins["gold"] * 1000 >= cost
    elif denomination == "silver":
        return coins["silver"] * 100 >= cost
    else:  # copper
        return coins["copper"] >= cost


def pay_with_denomination(cost_in_coins, payment_coins, denomination, amount):
    """
    Calculate total cost in copper first, then convert to chosen denomination
    """
    # Calculate total cost in copper, multiplying by amount being purchased
    total_cost = (
        cost_in_coins["gold"] * 1000
        + cost_in_coins["silver"] * 100
        + cost_in_coins["copper"]
    ) * amount  # Need to add amount parameter

    if denomination == "gold":
        cost_in_chosen = (total_cost + 999) // 1000  # Round up to nearest gold
        if payment_coins["gold"] >= cost_in_chosen:
            payment_coins["gold"] -= cost_in_chosen
            change = cost_in_chosen * 1000 - total_cost
            payment_coins["copper"] += change
            return payment_coins, True
    elif denomination == "silver":
        cost_in_chosen = (total_cost + 99) // 100  # Round up to nearest silver
        if payment_coins["silver"] >= cost_in_chosen:
            payment_coins["silver"] -= cost_in_chosen
            change = cost_in_chosen * 100 - total_cost
            payment_coins["copper"] += change
            return payment_coins, True
    elif denomination == "copper":
        if payment_coins["copper"] >= total_cost:
            payment_coins["copper"] -= total_cost
            return payment_coins, True

    return payment_coins, False


def visit_market(wagon, city, cities_idx):
    while True:
        market = city
        Price_Calculator(market, "corn")
        print("1.  Corn: " + Money_Converter(market["corn"]["moving_price"]))
        Price_Calculator(market, "iron_ore")
        print("2.  Iron Ore: " + Money_Converter(market["iron_ore"]["moving_price"]))
        print("3.  Go back")
        action = input()

        if action == "1":
            print("Amount to trade?")
            item = "corn"
            amount = int(input())
            wagon, cities_idx = market_interact(market, wagon, item, amount, cities_idx)

        elif action == "2":
            print("Amount to trade?")
            item = "iron_ore"
            amount = int(input())
            wagon, cities_idx = market_interact(market, wagon, item, amount, cities_idx)

        elif action == "3":
            break

    return wagon, cities_idx
