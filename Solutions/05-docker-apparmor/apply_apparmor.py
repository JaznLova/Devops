import docker


def main():
    client = docker.from_env()
    print("Building flask-apparmor:1.0...")
    client.images.build(path=".", tag="flask-apparmor:1.0")
    container = client.containers.run(
        "flask-apparmor:1.0",
        name="flask-apparmor-lab",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=flask-apparmor"],
        detach=True,
        remove=True,
    )
    try:
        details = client.api.inspect_container(container.id)
        print("Container:", container.short_id)
        print("Security options:", details["HostConfig"]["SecurityOpt"])
        input("Press Enter to stop the container...")
    finally:
        container.stop(timeout=5)


if __name__ == "__main__":
    main()
