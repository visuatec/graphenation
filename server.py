from flask import Flask, render_template, request
from crypto import get_crypto
from crypto_symbols import get_crypto_symbols
from waitress import serve
from datetime import datetime

app = Flask(__name__)

crypto_symbols = get_crypto_symbols()
symbols = crypto_symbols["symbols"]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", symbols=symbols)


@app.route("/crypto")
def get_crypto_data():
    crypto = request.args.get("crypto")

    # Check for empty strings or string with only spaces
    if not bool(crypto.strip()):
        # You could render "crypto Not Found" instead like we do below
        crypto = "BTCUSDT"
        print("No crypto provided, using default")

    crypto_data = get_crypto(crypto)

    # crypto is not found by API
    if "error" in crypto_data:
        return render_template(
            "crypto-not-found.html",
            full_data=crypto_data,
            symbols=symbols,
        )

    # format the price to 2 decimal places and usd currency
    unix_timestamp = crypto_data["timestamp"]

    # Convert Unix timestamp to datetime
    dt_object = datetime.utcfromtimestamp(unix_timestamp)

    return render_template(
        "crypto.html",
        full_data=crypto_data,
        title=crypto_data["symbol"],
        price="${:,.4f}".format(float(crypto_data["price"])),
        timestamp=dt_object.strftime("%Y-%m-%d %H:%M:%S"),
        symbols=symbols,
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
