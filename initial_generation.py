import random


def Player_Initialization():
    player = {
        "name": None,
        "city": None,
    }
    return player


def Wagon_Initialization():
    wagon = {
        "name": {None},
        "horse": {None},
        "cart": {"gold": 0, "silver": random.randint(20, 80), "copper": 0},
    }
    return wagon


def Feldor_Initialization():  # input: None, Output:  Feldor Dictionary
    feldor = {
        "name": "Feldor",
        "intro_text": [None],
        "exchange_fees": {
            "cs": 1,
            "sg": 1,
            "gs": 1,
            "sc": 1,
        },
        "corn": {
            "supply": random.randint(1000, 1700),
            "base_price": 10,
            "variance": 0.1,
            # moving_price: ...
        },
        "iron_ore": {
            "supply": random.randint(0, 500),
            "base_price": 100,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    return feldor


def Crankston_Initialization():  # input: None, Output:  Crankston Dictionary
    crankston = {
        "name": "Crankston",
        "intro_text": [None],
        "exchange_fees": {
            "cs": 1,
            "sg": 1,
            "gs": 1,
            "sc": 1,
        },
        "corn": {
            "supply": random.randint(250, 500),
            "base_price": 10,
            "variance": 0.1,
            # moving_price: ...
        },
        "iron_ore": {
            "supply": random.randint(500, 1000),
            "variance": 0.3,
            "base_price": 100,
            # moving_price: ...
        },
    }
    return crankston


def Tetra_Tower_Initialization():  # input: None, Output:  Tetra Tower Dictionary
    tetra_tower = {
        "name": "Tetra Tower",
        "intro_text": [None],
        "exchange_fees": {
            "cs": 1,
            "sg": 1,
            "gs": 1,
            "sc": 1,
        },
        "corn": {
            "supply": random.randint(3200, 8000),
            "base_price": 10,
            "variance": 0.1,
            # moving_price: ...
        },
        "iron_ore": {
            "supply": random.randint(1000, 1200),
            "base_price": 100,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    return tetra_tower


def Cabella_Initialization():  # input: None, Output:  Cabella Dictionary
    cabella = {
        "name": "Cabella",
        "intro_text": [None],
        "exchange_fees": {
            "cs": 1,
            "sg": 1,
            "gs": 1,
            "sc": 1,
        },
        "corn": {
            "supply": random.randint(1300, 4500),
            "base_price": 10,
            "variance": 0.1,
            # moving_price: ...
        },
        "iron_ore": {
            "supply": random.randint(130, 452),
            "base_price": 100,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    return cabella


def Foyella_Initialization():  # input: None, Output:  Foyella Dictionary
    foyella = {
        "name": "Foyella",
        "intro_text": [None],
        "exchange_fees": {
            "cs": 1,
            "sg": 1,
            "gs": 1,
            "sc": 1,
        },
        "corn": {
            "supply": random.randint(2000, 4500),
            "base_price": 10,
            "variance": 0.1,
            # moving_price: ...
        },
        "iron_ore": {
            "supply": random.randint(200, 300),
            "variance": 0.3,
            "base_price": 100,
            # moving_price: ...
        },
    }
    return foyella
