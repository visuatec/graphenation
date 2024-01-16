from bs4 import BeautifulSoup
import requests
import re


def get_exchange_rate(curr_one, curr_two):
    url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={curr_one}&To={curr_two}"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")
    something = (
        soup.find("p", class_="result__BigRate-sc-1bsijpp-1 dPdXSB")
        .text.split()[0]
        .replace(",", "")
    )
    return something


if __name__ == "__main__":
    print("\n*** Get Exchange Rate ***\n")

    currency_one = input("\nPlease enter Currency 1:")
    currency_two = input("\nPlease enter Currency 2:")
    exchange_rate = get_exchange_rate(currency_one, currency_two)
    # test with BTCUSDT

    print("\n")
    print("${:,.4f}".format(float(exchange_rate)))
