# from app.utils.task_scheduler import send_mail, send_sms
from flask_mail import Message
from app import mail
from config import Config
from flask import render_template


class NotificationService:

    def send_mail(self, email_info: dict):
        # send_mail.delay(email_info)
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

    # def send_sms(self, sms_info: dict):
    #     # send_sms.delay(sms_info)
