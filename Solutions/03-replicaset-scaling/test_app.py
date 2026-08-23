import unittest

from app import app


class FlashSaleTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "healthy")

    def test_buy_uses_requested_user(self):
        response = self.client.get("/buy?user=student-1")
        payload = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload["user"], "student-1")
        self.assertEqual(payload["status"], "success")


if __name__ == "__main__":
    unittest.main()
