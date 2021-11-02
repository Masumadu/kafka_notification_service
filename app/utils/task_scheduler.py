import pika
from pika import exceptions
import json


def create_email_queue(customer_info: dict):
    body = {
        "user": customer_info,
    }
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters
                                             (host="localhost"))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to the server")
        return

    channel = connection.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=json.dumps(body),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )
    connection.close()
    print(f"sent {customer_info}")
















# from app.extensions import celery
# from app import mail
# from flask_mail import Message
# from flask import render_template
#
#
# @celery.task
# def send_email(user, token):
#     msg = Message(
#         subject='Testing Emali Configuration',
#         sender='flask_app@test.com',
#         recipients=['paul@mailtrap.io'],
#         html=render_template("mail.html", user=user, token=token)
#     )
#     mail.send(msg)







# EMAIL_PROVIDER_API = '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'
#
#
# @shared_task
# def send_email(email_parameters):
#     try:
#         sg = sendgrid.SendGridAPIClient(
#             api_key=EMAIL_PROVIDER_API)
#         msg = Mail(**email_parameters)
#         sg.send(msg)
#     except Exception as e:
#         raise AppException.OperationError(context=e.args[0])
