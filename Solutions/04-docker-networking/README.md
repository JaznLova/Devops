# Exercise 4 - Docker Networking

Date: 2026-09-06

The Compose file creates one user-defined bridge network and connects the
Flask, MySQL, and Redis containers to it.

```bash
docker compose up --build -d
docker network inspect my-bridge-net
curl http://localhost:5001/about
curl http://localhost:5001/network-check
```

The network check should resolve both `mysql` and `redis` through Docker's
internal DNS. Run `python -m unittest -v` for the API test.

Clean up with `docker compose down -v`.
