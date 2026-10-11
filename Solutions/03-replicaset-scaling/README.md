# Exercise 3 - ReplicaSet Scaling

Date: 2026-08-23

```bash
minikube start --nodes=1
minikube image build -t flashsale:1.0 .
kubectl apply -f flashsale-replicaset.yaml
kubectl get rs,pods -l app=flashsale
kubectl scale rs flashsale-rs --replicas=5
kubectl get rs,pods -l app=flashsale
```

Delete any one listed Pod and run the final command again. The ReplicaSet should
create a replacement Pod automatically:

```bash
kubectl delete pod POD_NAME
kubectl get pods -l app=flashsale --watch
```

Use `minikube service flashsale-svc --url` and call `/buy?user=student-1` to
observe which Pod handled each request. Run `python -m unittest -v` for the app
tests. Clean up with `kubectl delete -f flashsale-replicaset.yaml`.
