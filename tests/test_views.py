from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_many_products(self):
        response = self.client.get("/api/v1/produits")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2)
    
    def test_read_one_product_missing_id(self):
        response = self.client.get("/api/v1/products")
        self.assert_404(response)
        
    def test_read_one_product(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertIn('name', product)
        
    def test_read_one_non_existing_product(self):
        response = self.client.get("/api/v1/products/0")
        self.assert_404(response)
