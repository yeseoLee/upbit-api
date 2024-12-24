from pprint import pprint
import requests


SERVER_URL = "https://api.upbit.com"

params = {"markets": "KRW-BTC"}

res = requests.get(SERVER_URL + "/v1/ticker", params=params)
pprint(res.json())
