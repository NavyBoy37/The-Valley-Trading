from running_functions import Money_Converter, Price_Calculator


def display_coins(coins):  # TIED TO market_interact()
    """Display exactly what coins are in possession"""
    return f"{coins['gold']}g {coins['silver']}s {coins['copper']}c"


def market_interact(market, wagon, item, amount):
    if amount == 0:
        print("Please enter a non-zero amount")
        return wagon

    cart = wagon["cart"]

    if amount > 0:  # Buying
        if amount > market[item]["supply"]:
            print(f"The market doesn't have enough {item} in stock")
            return wagon

        # Get raw price per unit
        unit_price = {
            "gold": market[item]["moving_price"] // 1000,
            "silver": (market[item]["moving_price"] % 1000) // 100,
            "copper": market[item]["moving_price"] % 100,
        }

        print(f"Cost per unit: {display_coins(unit_price)}")
        print(f"Current funds: {display_coins(cart)}")
        print("Choose payment method:")
        print("1. Gold pieces")
        print("2. Silver pieces")
        print("3. Copper pieces")
        print("4. Cancel transaction")

        choice = input()

        if choice == "4":
            return wagon

        denomination = {"1": "gold", "2": "silver", "3": "copper"}[choice]

        # Let player handle the math - just try to pay with what they chose
        result_coins, success = pay_with_denomination(
            unit_price, cart, denomination, amount
        )
        if not success:
            print(f"Insufficient {denomination} pieces")
            return wagon

        cart = result_coins
        market[item]["supply"] -= amount
        print(f"You bought {amount} {item}")

    elif amount < 0:  # Selling
        sell_amount = abs(amount)

        # Calculate raw profit in copper pieces
        profit = {"copper": market[item]["moving_price"] * sell_amount}

        # Add profit as copper pieces - let player convert later if desired
        cart["copper"] += profit["copper"]
        market[item]["supply"] += sell_amount
        print(f"You sold {sell_amount} {item} for {profit['copper']} copper pieces")

    wagon["cart"] = cart
    return wagon


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
            wagon["cart"]["copper"] -= 100 + exchange_fees["cs"]
            wagon["cart"]["silver"] += 1
            print(
                f"Converted 100 copper to 1 silver. Paid {exchange_fees['cs']} copper fee."
            )

        elif choice == "2" and wagon["cart"]["silver"] >= (10 + exchange_fees["sg"]):
            wagon["cart"]["silver"] -= 10 + exchange_fees["sg"]
            wagon["cart"]["gold"] += 1
            print(
                f"Converted 10 silver to 1 gold. Paid {exchange_fees['sg']} silver fee."
            )

        elif choice == "3" and wagon["cart"]["gold"] >= 1:
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
            wagon["cart"]["silver"] -= 1
            wagon["cart"]["copper"] += 100 - exchange_fees["sc"]
            print(
                f"Converted 1 silver to {100 - exchange_fees['sc']} copper. Paid {exchange_fees['sc']} copper fee."
            )

        elif choice == "5":
            break
        else:
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


def visit_market(
    wagon, city
):  # input: wagon dictionary, city dictionary, Output: wagon dictionary
    while True:
        market = city
        Price_Calculator(market, "corn")
        print("1.  Corn: " + Money_Converter(market["corn"]["moving_price"]))
        Price_Calculator(market, "iron_ore")
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
