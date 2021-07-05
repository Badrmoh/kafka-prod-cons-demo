# A simple kafka environment in action
## Description
Docker Compose is used to run all of the services. Docker Compose DNS is used for communication between services. Default values can be overwritten in a `.env` file. Running the app will build the python apps docker images once, before starting the app. Access the app after starting at http://localhost:5000
## Usage
```
docker-compose build
docker-compose up
```
## Information
- To stop docker compose, use `docker-compose down`. 
- If docker-compose services are killed, you will need to run the command above to clean any volumes.