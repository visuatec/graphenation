from flask import Flask, render_template, request
from crypto import get_crypto
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/crypto")
def get_crypto_data():
    crypto = request.args.get("crypto")

    # Check for empty strings or string with only spaces
    if not bool(crypto.strip()):
        # You could render "crypto Not Found" instead like we do below
        crypto = "BTC"
        print("No crypto provided, using default")

    crypto_data = get_crypto(crypto)

    # crypto is not found by API
    if "error" in crypto_data:
        return render_template(
            "crypto-not-found.html",
            full_data=crypto_data,
        )
    # if not crypto_data["code"] == 200:
    #     return render_template("crypto-not-found.html")
    # format the price to 2 decimal places and usd currency

    return render_template(
        "crypto.html",
        full_data=crypto_data,
        title=crypto_data["symbol"],
        price="${:,.4f}".format(float(crypto_data["price"])),
        # format timestamp below
        # timestamp=crypto_data["timestamp"].replace("T", " ").replace("Z", ""),
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
