from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_crypto_symbols():
    url = "https://api.api-ninjas.com/v1/cryptosymbols"
    response = requests.get(url, headers={"X-Api-Key": f"{os.getenv('NINJA_API_KEY')}"})

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return f"Error:, {response.status_code}, {response.text}"


if __name__ == "__main__":
    print("\n*** Getting ALL Crypto Symbols ***\n")
    crypto_data = get_crypto_symbols()
    print("\n")
    pprint(crypto_data)
