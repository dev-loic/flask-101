# pylint: disable=missing-docstring

from flask import Flask, jsonify, abort
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
}

@app.route('/api/v1/produits')
def retrieveProducts():
    return jsonify(list(PRODUCTS.values()))

# READ
@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def retrieveProduct(product_id):
    products = list(PRODUCTS.values())
    filtered_products = [product for product in products if product['id'] == product_id]
    if len(filtered_products) != 1:
        abort(404)
    else:
        return filtered_products[0]
    
# DELETE
@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def deleteProduct(product_id):
    element_to_delete = PRODUCTS.pop(product_id, None)
    if element_to_delete is None:
        abort(404)
    else:
        return ('', 204)
