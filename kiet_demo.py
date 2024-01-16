import requests
import json
from pprint import pprint

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()
pprint(data)
print(data["rates"]["INR"])
print(data["rates"]["EUR"])
print(data["rates"]["GBP"])
print(data["rates"]["CAD"])
print(data["rates"]["AUD"])
print(data["rates"]["JPY"])
print(data["rates"]["CHF"])
