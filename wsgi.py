# pylint: disable=missing-docstring

from flask import Flask
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
}

@app.route('/api/v1/produits')
def hello():
    return PRODUCTS
