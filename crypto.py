from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_crypto(crypto="BTC"):
    request_url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto}USDT"

    crypto_data = requests.get(request_url).json()
    return crypto_data


if __name__ == "__main__":
    print("\n*** Get Crypto Details ***\n")

    crypto = input("\nPlease enter a Crypto Currency :")
    crypto_data = get_crypto(crypto)

    print("\n")
    pprint(crypto_data)
