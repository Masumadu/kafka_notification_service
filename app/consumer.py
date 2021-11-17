import json
import os
from kafka import KafkaConsumer
import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv
from loguru import logger

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

BACKEND_SERVER = os.getenv("BACKEND_SERVER", default="localhost")

KAFKA_SUBSCRIPTIONS = os.getenv("KAFKA_SUBSCRIPTIONS")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
KAFKA_CONSUMER_GROUP_ID = os.getenv("KAFKA_CONSUMER_GROUP_ID")

subscriptions = KAFKA_SUBSCRIPTIONS.split("|")
bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS.split("|")

logger.info(f"KAFKA BOOTSTRAP SERVERS -> {bootstrap_servers}")

logger.info("_____CONNECTING TO SERVER_____")

consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset="earliest",
    group_id=KAFKA_CONSUMER_GROUP_ID,
    value_deserializer=lambda value: json.loads(value),
)
consumer.subscribe(subscriptions)

logger.info("_____CONSUMER STARTED_____")
for msg in consumer:
    logger.info(f"____kafka message {msg.value}_____")
    logger.error(f"_____topic consuming: {msg.topic}_____")
    logger.info("_____message received_____")
    if msg.value.get("service_channel") == "email":
        logger.info("_____processing mail message_____")
        try:
            requests.post(
                url=f"http://{BACKEND_SERVER}:5001/api/customer/send_mail",
                params=msg.value)
        except RequestException as exc:
            raise Exception(exc.args)
        logger.info("_____mail message consumed successfully_____")

    if msg.value.get("service_channel") == "sms":
        logger.info("_____processing sms message_____")
        try:
            requests.post(
                url=f"http://{BACKEND_SERVER}:5001/api/customer/send_sms",
                params=msg.value)
        except RequestException as exc:
            raise Exception(exc.args)
        logger.info("_____sms message consumed successfully_____")