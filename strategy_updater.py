# This script updates the strategy of the bot by retrieving it from GitHub

import json
import commentjson
import requests
from datetime import datetime

base_folder = "/user_data"


def update_strategy():
    # Retrieve new strategy from GitHub and write it to the file
    url = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/NostalgiaForInfinityX.py"
    with open(base_folder + "/strategies/NostalgiaForInfinityX.py", 'w+') as file:
        r = requests.get(url)
        file.write(r.text)


def update_blacklist():
    # Read the config file and parse to JSON
    with open(base_folder + '/config.json', "r") as file:
        json_object = json.load(file)

    # Retrieve the blacklist from GitHub
    url = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/configs/blacklist-kucoin.json"
    r = requests.get(url)

    # Read the blacklist coins from the JSON and put them in the config
    pair_blacklist = commentjson.loads(r.text)["exchange"]["pair_blacklist"]
    json_object["exchange"]["pair_blacklist"] = pair_blacklist

    with open(base_folder + '/config.json', "w") as file:
        json.dump(json_object, file, indent=4)


def update_pairlist():
    # Read the config file and parse to JSON
    with open(base_folder + '/config.json', "r") as file:
        json_object = json.load(file)

    # Retrieve the pairlists from GitHub
    url = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/configs/pairlist-volume-kucoin-usdt.json"
    r = requests.get(url)

    # Read the pairlists from the JSON and put them in the config
    pairlist = commentjson.loads(r.text)["pairlists"]
    json_object["pairlists"] = pairlist

    with open(base_folder + '/config.json', "w") as file:
        json.dump(json_object, file, indent=4)


def reload_config():
    # Read the config file and parse to JSON
    with open(base_folder + '/config.json', "r") as file:
        json_object = json.load(file)

    # Set the url, username and password
    url = "http://172.18.0.20:8080/api/v1/reload_config"
    username = json_object["api_server"]["username"]
    password = json_object["api_server"]["password"]

    # Reload the bot
    response = requests.post(url, auth=(username, password))
    print(response.text)


if __name__ == '__main__':
    update_strategy()
    update_blacklist()
    update_pairlist()
    print(str(datetime.now()) + " - Updated the strategy and pair lists.")
    reload_config()
