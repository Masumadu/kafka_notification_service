from flask_mail import Message
from app import mail
from app.extensions import celery
from config import Config
from flask import render_template


@celery.task
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


@celery.task
def send_sms(sms_info: dict):
    msg = Message(
        subject='Testing Celery SMS Configuration',
        sender='flask_app@test.com',
        recipients=['paul@mailtrap.io'],
        body="This is the sms test",
        html="<h1> Sms Test </h1>"
    )
    mail.send(msg)

















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
