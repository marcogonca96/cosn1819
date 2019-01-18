# COSN1819 

![alt text](https://github.com/marcogonca96/cosn1819/blob/master/trailerflix.png)


Netflix-like app but for trailers only
##### Project associated with FEUP


## Deploy on Kubernetes (locally)

### Prerequisites
- Minikube - https://github.com/kubernetes/minikube
- kubectl - https://kubernetes.io/docs/tasks/tools/install-kubectl
- Kompose - https://github.com/kubernetes/kompose

### Deployment
1. $ minikube start
2. $ minikube addons enable ingress
3. $ docker login (username: trailerflix | password: cosn1819)
4. $ kompose up (in the root, where docker-compose.yaml is) (wait for it to finish)
5. $ kubectl create -f ingresses/all.yaml
6. $ minikube dashboard (optional, to see the state of the deployment)
7. associate the minikube ip to the name "trailerflix" on etc/hosts
8. run the app by opening a browser and accessing http://trailerflix
