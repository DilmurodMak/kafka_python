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

## Event Hub Version

Create Event Hubs namespace and event hub in Azure Portal. Install required event hub python library

```python
 pip install azure-eventhub
```

```python
 pip install azure-eventhub-checkpointstoreblob-aio
```

Under the `eventhub\` directory there are two files `eventhub_consumer.py` and `eventhub_producer.py`. Copy event hub namespace connection string and eventhub name from newly create eventhub in azure. Paste the copied connection string and name in the required fields of consumer and producer files. Run both files side by side.
