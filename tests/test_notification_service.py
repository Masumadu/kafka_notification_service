from tests import BaseTestCase
import pytest
import unittest
from app.services.notification_service import NotificationService
from unittest.mock import patch
from app.utils.task_scheduler import send_mail, send_sms

notification_service = NotificationService()

email_parameters = {
    "from_email": "michaelasumadu1@outlook.com",
    "to_emails": "michaelasumadu1@gmail.com",
    "subject": f"Invoice",
    "html_content": "<b> name</b>"
}


class TestNotificationService(BaseTestCase):
    @pytest.mark.active
    def test_notification_send_mail(self):
        with patch.object(send_mail, "delay") as mock_send_mail:
            notification_service.send_mail(email_parameters)
        self.assertTrue(mock_send_mail.called)
        self.assertEqual(mock_send_mail.call_count, 1)

    @pytest.mark.active
    def test_notification_send_sms(self):
        with patch.object(send_sms, "delay") as mock_send_sms:
            notification_service.send_sms(email_parameters)
        self.assertTrue(mock_send_sms.called)
        self.assertEqual(mock_send_sms.call_count, 1)


if __name__ == "__main__":
    unittest.main()
