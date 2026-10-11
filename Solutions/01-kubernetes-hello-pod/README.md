# Exercise 1 - Kubernetes Hello Pod

Date: 2026-08-08

This manifest runs the Nginx storefront as a Pod and exposes it through a
NodePort Service.

```bash
minikube start
kubectl apply -f hello-k8s.yaml
kubectl wait --for=condition=Ready pod/hello-k8s --timeout=120s
kubectl get pod,service -l app=hello-k8s
minikube service hello-k8s
```

Expected result: the browser displays the Nginx welcome page.

Clean up with `kubectl delete -f hello-k8s.yaml`.
