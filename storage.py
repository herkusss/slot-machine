import json

def save_balance(player_name, balance, filename="balance.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[player_name] = balance
    with open(filename, "w") as f:
        json.dump(data, f)

def load_balance(player_name, filename="balance.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return data.get(player_name, 500)
    except FileNotFoundError:
        return 500

def get_all_players(filename="balance.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return list(data.keys())
    except FileNotFoundError:
        return []
