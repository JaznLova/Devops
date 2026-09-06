import unittest

from app import app


class ApiTest(unittest.TestCase):
    def test_about(self):
        response = app.test_client().get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Simple REST API")


if __name__ == "__main__":
    unittest.main()
