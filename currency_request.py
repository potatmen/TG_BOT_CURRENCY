import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_usd_to_rub():

    API_TOKEN = os.getenv("CURRENCY_SERVICE_API_KEY")
    url = f'https://v6.exchangerate-api.com/v6/{API_TOKEN}/latest/USD'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rub_rate = data['conversion_rates']['RUB']
        return rub_rate
    else:
        return None
