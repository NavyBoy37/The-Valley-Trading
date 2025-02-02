import random


def Feldor_Initialization():  # input: None, Output:  Feldor Dictionary
    feldor = {
        "name": "Crankston",
        "corn": {
            "supply": random.randint(1000, 1700),
            "base_price": 10,
            "variance": 0.1,
        },
        "iron_ore": {
            "supply": random.randint(0, 500),
            "base_price": 100,
            "variance": 0.3,
        },
    }
    return feldor


def Crankston_Initialization():  # input: None, Output:  Crankston Dictionary
    crankston = {
        "name": "Crankston",
        "corn": {
            "supply": random.randint(250, 500),
            "base_price": 10,
            "variance": 0.1,
        },
        "iron_ore": {
            "supply": random.randint(500, 1000),
            "variance": 0.3,
            "base_price": 100,
        },
    }
    return crankston


def Tetra_Tower_Initialization():  # input: None, Output:  Tetra Tower Dictionary
    tetra_tower = {
        "name": "Tetra Tower",
        "corn": {
            "supply": random.randint(3200, 8000),
            "base_price": 10,
            "variance": 0.1,
        },
        "iron_ore": {
            "supply": random.randint(1000, 1200),
            "base_price": 100,
            "variance": 0.3,
        },
    }
    return tetra_tower


def Cabella_Initialization():  # input: None, Output:  Cabella Dictionary
    cabella = {
        "name": "Cabella",
        "corn": {
            "supply": random.randint(1300, 4500),
            "base_price": 10,
            "variance": 0.1,
        },
        "iron_ore": {
            "supply": random.randint(130, 452),
            "base_price": 100,
            "variance": 0.3,
        },
    }
    return cabella


def Foyella_Initialization():  # input: None, Output:  Foyella Dictionary
    foyella = {
        "name": "Foyella",
        "corn": {
            "supply": random.randint(2000, 4500),
            "base_price": 10,
            "variance": 0.1,
        },
        "iron_ore": {
            "supply": random.randint(200, 300),
            "variance": 0.3,
            "base_price": 100,
        },
    }
    return foyella
