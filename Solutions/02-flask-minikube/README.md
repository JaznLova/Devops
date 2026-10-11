# Exercise 2 - Flask on Minikube

Date: 2026-08-16

```bash
minikube start
minikube image build -t flask-app:1.0 .
kubectl apply -f flask-deployment.yaml
kubectl rollout status deployment/flask-app
kubectl get pods,services -l app=flask-app
minikube service flask-app-service --url
```

Open the printed URL or pass it to `curl`. The expected response is
`Hello from Flask on Kubernetes!`.

Run the unit tests with `python -m unittest -v`. Clean up with
`kubectl delete -f flask-deployment.yaml`.
