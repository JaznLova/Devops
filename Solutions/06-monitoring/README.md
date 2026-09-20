# Exercise 6 - Prometheus and Grafana Monitoring

Date: 2026-09-06

This stack runs the delivery simulator, Prometheus, and Grafana on one Compose
network. The Prometheus data source is provisioned automatically.

```bash
docker compose up --build -d
curl http://localhost:8000/metrics
```

- Metrics: <http://localhost:8000/metrics>
- Prometheus targets and alerts: <http://localhost:9090/targets>
- Grafana: <http://localhost:3000> (`admin` / `devops-lab-only`)

In Grafana, create panels using `pending_deliveries`,
`on_the_way_deliveries`, and `average_delivery_time_seconds`. The generated
values intentionally cross the supplied alert thresholds.

Run `python -m unittest -v` for the simulator test. Clean up with
`docker compose down -v`.
