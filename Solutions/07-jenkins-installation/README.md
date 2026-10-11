# Exercise 7 - Jenkins CI Installation

Date: 2026-09-27

The custom image installs the Git and Pipeline plugins during the image build,
and a named volume preserves Jenkins configuration.

```bash
docker compose up --build -d
docker compose ps
docker compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Open <http://localhost:8080>, enter the printed one-time password, and complete
the local setup wizard. Verify the installation from **Manage Jenkins >
Plugins** and confirm that Git and Pipeline are installed.

Stop Jenkins with `docker compose down`. Add `-v` only when you intentionally
want to delete all local Jenkins configuration and jobs.
