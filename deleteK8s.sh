#!/bin/bash

kubectl delete deployment --all
kubectl delete pod --all
kubectl delete svc --all
kubectl delete pvc --all