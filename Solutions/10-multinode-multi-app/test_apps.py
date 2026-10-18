import unittest

import product_catalog
import shopping_cart


class ProductCatalogTest(unittest.TestCase):
    def test_products(self):
        response = product_catalog.app.test_client().get("/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 3)


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        shopping_cart.cart.clear()
        self.client = shopping_cart.app.test_client()

    def test_add_and_read_item(self):
        item = {"id": 1, "name": "Laptop", "quantity": 1}
        response = self.client.post("/cart", json=item)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), [item])
        self.assertEqual(self.client.get("/cart").get_json(), [item])

    def test_rejects_non_json_request(self):
        response = self.client.post("/cart", data="not-json")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
