import requests
import pandas as pd

def fetch_data(api_url, token, params=None):
    headers = {"Flic-Token": token}
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None