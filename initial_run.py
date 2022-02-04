# This script initializes the bot with the values from the .env file

import os
import json
from dotenv import load_dotenv
from datetime import datetime
import secrets

load_dotenv()
base_folder = "/user_data"


def initiate_bot():
    # Cast the file to JSON
    with open(base_folder + '/config.json', "r") as file:
        json_object = json.load(file)

    # Change all values according to your .env file
    json_object["exchange"]["key"] = os.getenv("EXCHANGE_KEY")
    json_object["exchange"]["secret"] = os.getenv("EXCHANGE_SECRET")
    json_object["exchange"]["password"] = os.getenv("EXCHANGE_PASSWORD")

    json_object["telegram"]["token"] = os.getenv("TELEGRAM_TOKEN")
    json_object["telegram"]["chat_id"] = os.getenv("TELEGRAM_CHAT_ID")

    if json_object["api_server"]["jwt_secret_key"] == "":
        json_object["api_server"]["jwt_secret_key"] = secrets.token_hex()
        json_object["api_server"]["password"] = secrets.token_hex()

    # Save the altered JSON object to the file
    with open(base_folder + '/config.json', "w") as file:
        json.dump(json_object, file, indent=4)


if __name__ == '__main__':
    initiate_bot()
    print(str(datetime.now()) + " - Finished running the initial setup.")
