import json
import pika
from pika import exceptions
import requests
from requests.exceptions import RequestException

print(' Connecting to server ...')

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
        # pika.URLParameters("amqp://guest:guest@rabbitmq:5672/")
    )
except exceptions.AMQPConnectionError as exc:
    print("Failed to connect to RabbitMQ service. Message wont be sent.")
    raise Exception(exc.args)

channel = connection.channel()
channel.queue_declare(queue="notification", durable=True)

print(' Waiting for messages...')


def callback(ch, method, properties, body):
    print("message received!!!")
    message_body = json.loads(body)
    if message_body.get("service_channel") == "email":
        print("processing email queue!!!")
        try:
            requests.post(url="http://localhost:5002/api/customer/send_mail",
                          params=message_body)
            # requests.post(url="http://backend:5001/api/customer/send_mail",
            #               params=message_body)
        except RequestException as exc:
            raise Exception(exc.args)

    if message_body.get("service_channel") == "sms":
        print("processing sms queue!!!!")
        try:
            requests.post(url="http://localhost:5002/api/customer/send_sms",
                          params=message_body)
            # docker requests url
            # requests.post(url="http://backend:5001/api/customer/send_sms",
            #               params=message_body)
        except RequestException as exc:
            raise Exception(exc.args)

    print("Done!!!")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='notification', on_message_callback=callback)
channel.start_consuming()
