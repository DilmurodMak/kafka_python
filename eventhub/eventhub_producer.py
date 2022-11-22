import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from faker import Faker
import json
import time
import logging
import random 
fake=Faker()

EVENT_HUBS_NAMESPACE_CONNECTION_STRING = ""
EVENT_HUB_NAME = ""

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str=EVENT_HUBS_NAMESPACE_CONNECTION_STRING, eventhub_name=EVENT_HUB_NAME)
    
    for i in range(10):
        data={
        'user_id': fake.random_int(min=20000, max=100000),
        'user_name':fake.name(),
        'user_address':fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
        'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
        'signup_at': str(fake.date_time_this_month())    
        }
        m=json.dumps(data)
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData(m))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)
        time.sleep(3)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())