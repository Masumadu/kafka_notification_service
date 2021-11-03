import requests

from app.repositories import CustomerRepository
from app.services import NotificationService
from flask import url_for

notification_service = NotificationService()


class CustomerController:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def send_mail(self, customer_info: dict):
        notification_service.send_mail(customer_info)
        return {"status": "email sent"}

    # def send_sms(self, customer_info: dict):
    #     notification_service.send_sms(customer_info)
    #     return {"status": "sms sent"}

