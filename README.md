[![Build/Push Docker Images](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/docker.yml/badge.svg)](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/docker.yml)

# A simple kafka environment in docker containers

## Description
Kafka is a messaging and broker system that allows to send and receive real-time events/data. Such system is used widely in several projects like Sentry. Kafka is distinguished for its ability to run as a distributed system and storing large amounts of data without losing performance. This demo project demonstrates kafka's in a simple way by deploying services in side docker containers using different methods. Since this demo is part of the **Projects** initiative of the Suse Challenge Udacity Course, every collaborator is welcome to contribute using his own code.

## Services in the project
- Zookeeper: Credits to wurstmeister.
- Kafka: Credits to wurstmeister.
- python-producer: Combination of flask to handle the frontend and a kafka producer to publish data to kafka.
- python-consumer: Retrives new messages from kafka and sends them to python-producer endpoint to be viewed.

## Build Docker Images Manually
```bash
docker build -t <tag> -f Dockerfile ./python/kafka-prod/
docker build -t <tag> -f Dockerfile ./python/kafka-cons/
```

## Methods of deployment
### docker-compose
1. Use docker-compose with building images locally
```bash
docker-compose -f docker-compose.yaml build
docker-compose -f docker-compose.yaml up
```
2. Use docker-compose with pre-built images
```bash
docker-compose -f docker-compose-prebuilt.yaml build
docker-compose -f docker-compose-prebuilt.yaml up
```
### Kubernetes
In Progress
### Helm
Not Started
### ArgoCD
Not Started
---
## Author
Badr Ibrahim: engbdr0@gmail.com
## Contributors
Please, fork this repo and work on your copy. You can make a pull request, which will be reviewed before merging.
