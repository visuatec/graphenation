from bs4 import BeautifulSoup
import requests
import re
from xe_convert import get_exchange_rate


url = "https://sjc.com.vn/giavang/textContent.php"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

table = soup.find("table")

# Regular expression to match the category and the two amounts
pattern = r"Vàng nhẫn SJC 99,99  1 chỉ, 2 chỉ, 5 chỉ\s+(\d{2},\d{3},\d{3})\s+(\d{2},\d{3},\d{3})"

# Search the text
match = re.search(pattern, table.text)

if match:
    # Extract the amounts
    amount1, amount2 = match.groups()
    print("BUY :", amount1)  # The first amount (buying price)
    print("SELL:", amount2)  # The second amount (selling price)
    one_chi = int(amount1.replace(",", "")) / 10
    five_chi = one_chi * 5
    print(f"1 chi = {one_chi} VNĐ")
    print(f"5 chi = {five_chi} VNĐ")
    exchange_rate = float(get_exchange_rate("USD", "VND"))
    # round to 2 decimal places when printing
    print(f"1 chi = {one_chi/exchange_rate:.2f} USD")
    print(f"5 chi = {five_chi/exchange_rate:.2f} USD")
    print(f"5 rings are worth {(five_chi/exchange_rate)*5:.2f} USD")
else:
    print("Pattern not found")
