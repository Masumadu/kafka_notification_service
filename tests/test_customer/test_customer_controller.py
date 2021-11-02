from unittest.mock import patch

from tests import BaseTestCase
import pytest
import unittest
from app.services.notification_service import NotificationService
from app.utils.task_scheduler import send_mail, send_sms

notification_service = NotificationService()

NEW_DATA = {
    "name": "new_customer",
    "username": "new_customer_username",
    "email": "new_customer_email",
    "password": "new_customer_password"
}


class TestAdminController(BaseTestCase):
    @pytest.mark.customer
    def test_notification_send_mail(self):
        with patch.object(send_mail, "delay") as mock_celery_mail_delay:
            notification_service.send_mail(NEW_DATA)
        self.assertTrue(mock_celery_mail_delay.called)
        self.assertEqual(mock_celery_mail_delay.call_count, 1)

    @pytest.mark.customer
    def test_notification_send_sms(self):
        with patch.object(send_sms, "delay") as mock_celery_sms_delay:
            notification_service.send_sms(NEW_DATA)
        self.assertTrue(mock_celery_sms_delay.called)
        self.assertEqual(mock_celery_sms_delay.call_count, 1)


if __name__ == "__main__":
    unittest.main()
