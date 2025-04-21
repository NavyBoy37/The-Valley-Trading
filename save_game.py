import json
import os
import copy
from running_functions import spcr


def save_game(player, wagon, cities_idx, filename="the_valley_save.json"):
    # Create the save directory if it doesn't exist
    save_dir = "save"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Construct the full path
    save_path = os.path.join(save_dir, filename)

    # Create a deep copy to avoid modifying the original data
    wagon_copy = copy.deepcopy(wagon)

    # Convert sets to lists for JSON serialization
    if isinstance(wagon_copy["name"], set):
        wagon_copy["name"] = list(wagon_copy["name"])
    if isinstance(wagon_copy["horse"], set):
        wagon_copy["horse"] = list(wagon_copy["horse"])

    # Prepare the save data
    save_data = {"player": player, "wagon": wagon_copy, "cities_idx": cities_idx}

    # Write the save file
    with open(save_path, "w") as f:
        json.dump(save_data, f, indent=2)

    print(f"Game saved to {save_path}")
    return True


def load_game(filename="the_valley_save.json"):
    # Construct the full path
    save_path = os.path.join("save", filename)

    try:
        with open(save_path, "r") as f:
            save_data = json.load(f)

        # Convert lists back to sets
        if isinstance(save_data["wagon"]["name"], list):
            save_data["wagon"]["name"] = set(save_data["wagon"]["name"])
        if isinstance(save_data["wagon"]["horse"], list):
            save_data["wagon"]["horse"] = set(save_data["wagon"]["horse"])

        print(f"Game loaded from {save_path}")
        return save_data["player"], save_data["wagon"], save_data["cities_idx"]
    except FileNotFoundError:
        print(f"Save file not found at {save_path}!")
        return None, None, None
    except Exception as e:
        print(f"Error loading game: {str(e)}")
        return None, None, None


def list_save_files(save_directory):
    # Get list of all files in the directory
    save_files = [
        f
        for f in os.listdir(save_directory)
        if os.path.isfile(os.path.join(save_directory, f))
    ]

    # Print files with numbers for selection
    print("Please type and enter a listed save")
    spcr()
    for file in save_files:
        print(file)
    spcr()

    # Optional: Let user select a file

    return None
