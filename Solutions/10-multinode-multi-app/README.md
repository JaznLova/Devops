# Exercise 10 - Multi-Node, Multi-App Minikube Deployment

Date: 2026-10-18

This exercise deploys two Flask services across a three-node Minikube cluster.
Pod anti-affinity places the two Product Catalog replicas and three Shopping
Cart replicas on different nodes.

```bash
minikube start --nodes 3 -p devops-multinode
docker build -t product-catalog:1.0 -f Dockerfile.product .
docker build -t shopping-cart:1.0 -f Dockerfile.shopping .
minikube -p devops-multinode image load product-catalog:1.0
minikube -p devops-multinode image load shopping-cart:1.0

kubectl apply -f product_catalog_deployment.yaml
kubectl apply -f product_catalog_service.yaml
kubectl apply -f shopping_cart_deployment.yaml
kubectl apply -f shopping_cart_service.yaml
kubectl get pods -o wide
```

The Product Catalog should have two ready Pods on different nodes; Shopping
Cart should have three ready Pods, one per node. Obtain access URLs with:

```bash
minikube -p devops-multinode service product-catalog-service --url
minikube -p devops-multinode service shopping-cart-service --url
```

Test `/products`, `GET /cart`, and `POST /cart` as shown in the exercise. Run
the local application tests with `python -m unittest -v`.

The cart is intentionally in memory to match the exercise. With three replicas,
each Pod has independent state, so production code would require a shared data
store and should not rely on a later GET returning data written to another Pod.

Clean up with:

```bash
kubectl delete -f product_catalog_service.yaml -f product_catalog_deployment.yaml
kubectl delete -f shopping_cart_service.yaml -f shopping_cart_deployment.yaml
minikube delete -p devops-multinode
```
