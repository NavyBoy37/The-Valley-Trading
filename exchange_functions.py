from running_functions import spcr, display_coins


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
            spcr()
            break
        else:
            spcr()
            print("Invalid choice or insufficient coins")

    return wagon
