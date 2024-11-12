from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def route() -> str:
    return "<p>StockAPI</p>"


@app.route("/stock/<str:stock_symbol>", methods=['GET'])
def get_stock_symbol():
    pass


@app.route("/stock/<str:stock_symbol>", methods=['POST'])
def update_stock_symbol():
    pass
