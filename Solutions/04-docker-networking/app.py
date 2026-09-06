import socket

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/about")
def about():
    return jsonify(
        name="Simple REST API",
        version="1.0",
        description="A Flask API connected to MySQL and Redis containers.",
    )


@app.get("/network-check")
def network_check():
    services = {}
    for hostname in ("mysql", "redis"):
        try:
            services[hostname] = {"reachable": True, "ip": socket.gethostbyname(hostname)}
        except socket.gaierror:
            services[hostname] = {"reachable": False, "ip": None}
    status = 200 if all(item["reachable"] for item in services.values()) else 503
    return jsonify(services), status


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
