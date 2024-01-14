from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_crypto(crypto):
    url = f"https://api.api-ninjas.com/v1/cryptoprice?symbol={crypto}"
    response = requests.get(url, headers={"X-Api-Key": f"{os.getenv('NINJA_API_KEY')}"})

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return f"Error:, {response.status_code}, {response.text}"


if __name__ == "__main__":
    print("\n*** Get Crypto Details ***\n")

    crypto = input("\nPlease enter a Crypto Currency :")
    crypto_data = get_crypto(crypto)
    # test with BTCUSDT

    print("\n")
    print(crypto_data["symbol"])
    print("${:,.4f}".format(float(crypto_data["price"])))
    pprint(crypto_data)
