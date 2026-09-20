import random
import time

from prometheus_client import Gauge, start_http_server

total_deliveries = Gauge("total_deliveries", "Total number of deliveries")
pending_deliveries = Gauge("pending_deliveries", "Number of pending deliveries")
on_the_way_deliveries = Gauge(
    "on_the_way_deliveries", "Number of deliveries on the way"
)
average_delivery_time_seconds = Gauge(
    "average_delivery_time_seconds", "Current average delivery time in seconds"
)


def simulate_delivery():
    pending = random.randint(10, 20)
    on_the_way = random.randint(5, 20)
    delivered = random.randint(30, 70)
    average_seconds = random.uniform(15, 45)

    snapshot = {
        "total": pending + on_the_way + delivered,
        "pending": pending,
        "on_the_way": on_the_way,
        "average_seconds": average_seconds,
    }
    total_deliveries.set(snapshot["total"])
    pending_deliveries.set(snapshot["pending"])
    on_the_way_deliveries.set(snapshot["on_the_way"])
    average_delivery_time_seconds.set(snapshot["average_seconds"])
    return snapshot


def main():
    start_http_server(8000, addr="0.0.0.0")
    print("Metrics available on http://0.0.0.0:8000/metrics")
    while True:
        print(simulate_delivery(), flush=True)
        time.sleep(1)


if __name__ == "__main__":
    main()
