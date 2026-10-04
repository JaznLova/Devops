# Exercise 8 - Jenkins Hello World Job

Date: 2026-09-20

The shell script can be used in the handout's Freestyle job. This folder also
includes a Jenkinsfile so the same job can be kept as code.

For a Freestyle project, configure Git as source control and add an **Execute
shell** build step:

```bash
cd Solutions/08-jenkins-hello-world
sh hello-world.sh
```

For a Pipeline job, select **Pipeline script from SCM**, point Jenkins at this
repository, and use this script path:

```text
Solutions/08-jenkins-hello-world/Jenkinsfile
```

Expected console output includes `Hello, Jenkins!` followed by `Finished:
SUCCESS`.
