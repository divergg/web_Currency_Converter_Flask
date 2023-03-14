import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

"""Function that returns actual rate from API"""


def get_rates(cur_from: str, cur_to: str, amount: float) -> float:
    url = f"https://api.apilayer.com/currency_data/convert?to={cur_to}&from={cur_from}&amount={amount}"
    payload = {}
    headers = {
        "apikey": os.getenv('apikey')
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    result = data['result']

    return result
