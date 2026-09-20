import unittest
from unittest.mock import patch

import delivery_metrics


class DeliveryMetricsTest(unittest.TestCase):
    @patch("delivery_metrics.random.uniform", return_value=31.5)
    @patch("delivery_metrics.random.randint", side_effect=[12, 8, 40])
    def test_simulated_snapshot(self, _randint, _uniform):
        snapshot = delivery_metrics.simulate_delivery()
        self.assertEqual(snapshot["total"], 60)
        self.assertEqual(snapshot["pending"], 12)
        self.assertEqual(snapshot["on_the_way"], 8)
        self.assertEqual(snapshot["average_seconds"], 31.5)


if __name__ == "__main__":
    unittest.main()
