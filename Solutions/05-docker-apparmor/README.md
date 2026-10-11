# Exercise 5 - Docker Security with AppArmor

Date: 2026-09-13

AppArmor is available on Linux hosts; Docker Desktop on Windows cannot run this
profile directly. On an AppArmor-enabled Linux machine:

```bash
sudo install -m 0644 flask-apparmor /etc/apparmor.d/flask-apparmor
sudo apparmor_parser -r /etc/apparmor.d/flask-apparmor
docker build -t flask-apparmor:1.0 .
docker run --rm --security-opt apparmor=flask-apparmor -p 5000:5000 flask-apparmor:1.0
```

In another terminal, verify the app with `curl http://localhost:5000`. Install
the SDK requirements and use `python apply_apparmor.py` to inspect the applied
security option. Run `python test_restricted_actions.py` to confirm that reads
of `/etc/shadow` and `/etc/gshadow` fail.

Unload the lab profile with:

```bash
sudo apparmor_parser -R /etc/apparmor.d/flask-apparmor
```
