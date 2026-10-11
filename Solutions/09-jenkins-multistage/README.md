# Exercise 9 - Jenkins Multi-Stage Pipeline

Date: 2026-10-11

The pipeline builds an isolated Python environment, runs unit tests, copies the
deployable files to a mock deployment directory, performs a health-check smoke
test, and archives the deployment files.

Create a Jenkins Pipeline using **Pipeline script from SCM** and configure this
script path:

```text
Solutions/09-jenkins-multistage/Jenkinsfile
```

The Jenkins agent needs Python 3 with the `venv` module. For a local check:

```bash
python -m pip install -r requirements.txt
python -m unittest -v
```

Expected result: two tests pass and Jenkins reports all four stages as
successful.
