import docker


def main():
    client = docker.from_env()
    container = client.containers.run(
        "flask-apparmor:1.0",
        name="flask-apparmor-test",
        security_opt=["apparmor=flask-apparmor"],
        detach=True,
        remove=True,
    )
    try:
        for command in (["cat", "/etc/shadow"], ["cat", "/etc/gshadow"]):
            result = container.exec_run(command)
            print("Command:", " ".join(command))
            print("Exit code:", result.exit_code)
            print("Output:", result.output.decode(errors="replace"))
            if result.exit_code == 0:
                raise SystemExit("Restricted file was unexpectedly readable")
    finally:
        container.stop(timeout=5)


if __name__ == "__main__":
    main()
