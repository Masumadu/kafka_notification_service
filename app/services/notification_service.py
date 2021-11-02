from app.core.notifications import NotificationHandler
from app.schema import ReadCustomerSchema
from app import mail
from flask_mail import Message
from flask import render_template

customer_schema = ReadCustomerSchema()


class EmailNotification(NotificationHandler):
    customer_info: dict

    def send(self):
        msg = Message(
            subject='Testing Email Configuration',
            sender='flask_app@test.com',
            recipients=['paul@mailtrap.io'],
            body=render_template("verify_account.txt", username=self.customer_info.get("username"),
                                 url=self.customer_info.get("url")),
            html=render_template("verify_account.html", username=self.customer_info.get("username"),
                                 url=self.customer_info.get("url"))
        )
        mail.send(msg)
