import csv
import random

# initializes item weights for cart
ITEM_WEIGHTS = {
    # product weights
    "corn": 10,
    "iron_ore": 50,
    "pelts": 30,
    "gems": 5,
    "supplies": 12,
    # currency weights
    "gold": 1,
    "silver": 1,
    "gold": 1,
}
# initializes length of roads (determined by supplies used)
ROAD_LENGTHS = {
    "Road_Feldor_Cabella": 1,
    "Road_Cabella_Feldor": 1,
    "Road_Feldor_Foyella": 2,
    "Road_Foyella_Feldor": 2,
    "Road_Cabella_Foyella": 3,
    "Road_Foyella_Cabella": 3,
    "Road_Feldor_Crankston": 4,
    "Road_Crankston_Feldor": 4,
    "Road_Crankston_TetraTower": 5,
    "Road_TetraTower_Crankston": 5,
    "Road_Feldor_Hardrock": 6,
    "Road_Hardrock_Feldor": 6,
    "Road_Hardrock_Caralo": 7,
    "Road_Caralo_Hardrock": 7,
    "Road_Caralo_Cabella": 7,
    "Road_Cabella_Caralo": 7,
    "Road_Foyella_Silter": 8,
    "Road_Silter_Foyella": 8,
    "Road_Silter_Tobunia": 9,
    "Road_Tobunia_Silter": 9,
    "Road_Tobunia_Ratherberg": 10,
    "Road_Ratherberg_Tobunia": 10,
    "Road_Ratherberg_Silter": 11,
    "Road_Silter_Ratherberg": 11,
}


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
        "cart": {
            "gold": 500,
            "silver": random.randint(20, 80),
            "copper": 0,
            "supplies": 1,
            "corn": 0,
            "iron_ore": 0,
            "pelts": 0,
            "gems": 0,
        },
        "capacity": {
            # cart current fullness and capacity
            "max_weight": 1000,
            "current_weight": 0,
        },
    }
    return wagon


def Feldor_Initialization():  # input: None, Output:  Feldor Dictionary
    """
    This comment will refer to all city initialization functions below.
    This function is run in a position in the cities_idx list in main.py.  Cities_idx houses
    the perpetual and changing city information in the game.  The feldor dictionary houses
    name, a sublist of intro_text, money conversion fees, product base prices and supplies and variance.
    Each initialization also loads intro text from a csv into the sublist in the dictionary.
    I expect to use the .csv list loading method for many future purposes.
    """
    feldor = {
        "name": "Feldor",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            feldor["intro_text"].append(row["feldor_intro"])
    return feldor


def Crankston_Initialization():  # input: None, Output:  Crankston Dictionary
    crankston = {
        "name": "Crankston",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            crankston["intro_text"].append(row["crankston_intro"])

    return crankston


def Tetra_Tower_Initialization():  # input: None, Output:  Tetra Tower Dictionary
    tetra_tower = {
        "name": "TetraTower",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }

    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            tetra_tower["intro_text"].append(row["tetra_tower_intro"])
    return tetra_tower


def Cabella_Initialization():  # input: None, Output:  Cabella Dictionary
    cabella = {
        "name": "Cabella",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }

    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            cabella["intro_text"].append(row["cabella_intro"])
    return cabella


def Foyella_Initialization():  # input: None, Output:  Foyella Dictionary
    foyella = {
        "name": "Foyella",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            foyella["intro_text"].append(row["foyella_intro"])
    return foyella


def Hardrock_Initialization():  # input: None, Output:  Hardrock Dictionary
    hardrock = {
        "name": "Hardrock",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            hardrock["intro_text"].append(row["hardrock_intro"])
    return hardrock


def Caralo_Initialization():  # input: None, Output:  Caralo Dictionary
    caralo = {
        "name": "Caralo",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            caralo["intro_text"].append(row["caralo_intro"])
    return caralo


def Silter_Initialization():  # input: None, Output:  Silter Dictionary
    silter = {
        "name": "Silter",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            silter["intro_text"].append(row["silter_intro"])
    return silter


def Ratherberg_Initialization():  # input: None, Output:  Ratherberg Dictionary
    ratherberg = {
        "name": "Ratherberg",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            ratherberg["intro_text"].append(row["ratherberg_intro"])
    return ratherberg


def Tobunia_Initialization():  # input: None, Output:  Tobunia Dictionary
    tobunia = {
        "name": "Tobunia",
        "intro_text": [],
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
        "pelts": {
            "supply": random.randint(0, 500),
            "base_price": 50,
            "variance": 0.3,
            # moving_price: ...
        },
        "gems": {
            "supply": random.randint(0, 200),
            "base_price": 1000,
            "variance": 0.3,
            # moving_price: ...
        },
        "supplies": {
            "supply": random.randint(0, 25000),
            "base_price": 10,
            "variance": 0.3,
            # moving_price: ...
        },
    }
    # loads intro text into city dictionary
    with open("filler_text.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            tobunia["intro_text"].append(row["tobunia_intro"])
    return tobunia
