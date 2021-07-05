# A simple kafka environment in action
## Description
Kafka is a messaging and broker system that allows to send and receive real-time events/data. Such system is used widely in several projects like Sentry. Kafka is distinguished for its ability to run as a distributed system and storing large amounts of data without losing performance.
## Services in the project
- Zookeeper: Credits to wurstmeister.
- Kafka: Credits to wurstmeister.
- python-producer: Combination of flask to handle the frontend and a kafka producer to publish data to kafka.
- python-consumer: Retrives new messages from kafka and sends them to python-producer endpoint to be viewed.
## Methods of deployment
- docker-compose: Done
- Kubernetes: In Progress
- Helm: Not Started
- ArgoCD: Not Started
## Author
Badr Ibrahim: engbdr0@gmail.com
## Contributors
Please, don't overwrite any directory, rather push to a new directory with a descriptive title, or in a new branch.
