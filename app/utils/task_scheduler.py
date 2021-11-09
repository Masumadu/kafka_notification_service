from flask_mail import Message
from app import mail
from config import Config
from flask import render_template
from app.celery_app import app


@app.task
def send_mail(email_info: dict):
    msg = Message(
        subject='Testing Celery Email Configuration',
        sender=Config.ADMIN_EMAIL,
        recipients=[email_info.get("email")],
        body=render_template("verify_account.txt",
                             username=email_info.get("username"),
                             url=email_info.get("verification_link")),
        html=render_template("verify_account.html",
                             username=email_info.get("username"),
                             url=email_info.get("verification_link"))
    )
    mail.send(msg)


@app.task
def send_sms(sms_info: dict):
    msg = Message(
        subject='Testing Celery SMS Configuration',
        sender='flask_app@test.com',
        recipients=['paul@mailtrap.io'],
        body="This is the sms test",
        html="<h1> Sms Test </h1>"
    )
    mail.send(msg)
