# kafka_python

This is a simple example of running the Kafka on local docker container with producer and consumer in python language

## Prerequisites

- Docker installed locally
- Python installed locally and libraries (confluent-kafka, faker)

## Running the producer and client

Clone the project to your local machine. Ensure the docker is running. From the root directory run the bellow command. It will run docker-compose.yaml to start all kafka services in local docker container

```docker
docker-compose up -d 
```

Open two terminals and run `kafka_consumer.py` and `kafka_producer.py` side by side

```python
python kafka_consumer.py
```

```python
python kafka_producer.py
```

You should be able to see fake user info produced in the producer terminal will show up on the consumer terminal
