import json

def load_user_data(filename="user_data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(data, filename="user_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)