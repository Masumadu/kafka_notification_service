from flask_mail import Message
from app import mail
from flask import render_template
from app.celery_app import app
import requests
from requests import RequestException
import os
from loguru import logger


@app.task
def send_mail(email_info: dict):
    msg = Message(
        subject='Account Verification',
        sender=os.getenv("ADMIN_EMAIL"),
        recipients=[email_info.get("email")],
        body=render_template(
            "verify_account.txt", username=email_info.get("username"),
            url=email_info.get("verification_link")
        ),
        html=render_template(
            "verify_account.html", username=email_info.get("username"),
            url=email_info.get("verification_link")
        )
    )
    mail.send(msg)


@app.task
def send_sms(sms_info: dict):
    end_point = f"https://api.mnotify.com/api/sms/quick?key={os.getenv('MNOTIFY_API_KEY')}"
    data = {
        'recipient[]': ['0247049596'],
        'sender': 'Flask Team',
        'message': f"Login Attempt. Details\n"
                   f"Account_Username: {sms_info.get('account')}.\n"
                   f"Activity: {sms_info.get('activity')}\n"
                   f"Status: {sms_info.get('status')}",
        'is_schedule': False,
        'schedule_date': ''
    }
    try:
        response = requests.post(end_point, data)
    except RequestException as e:
        logger.error(f"Failed to contact sms provider with error {e}")
    else:
        response_data = response.json()
        if response_data['code'] == '2000':
            logger.info(f"sms successfully sent with response {response_data}")
        else:
            logger.info(f"error sending sms with response {response_data}")
