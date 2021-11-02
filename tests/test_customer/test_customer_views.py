import unittest
from tests import BaseTestCase
import pytest
from flask import url_for
from unittest.mock import patch
from app.utils.task_scheduler import send_mail, send_sms

NEW_DATA = {
    "name": "new_customer",
    "username": "new_customer_username",
    "email": "new_customer_email",
    "password": "new_customer_password"
}


class TestCustomerViews(BaseTestCase):
    @pytest.mark.customer
    def test_send_mail(self):
        with patch.object(send_mail, "delay") as mock_send_mail:
            response = self.client.post(
                url_for("customer.send_mail"), query_string=NEW_DATA
            )
        self.assert200(response)
        self.assertEqual(response.json, self.shared_responses.send_mail())
        self.assertTrue(mock_send_mail.called)
        self.assertEqual(mock_send_mail.call_count, 1)

    @pytest.mark.customer
    def test_send_sms(self):
        with patch.object(send_sms, "delay") as mock_send_sms:
            mock_send_sms.return_value = "sms sent"
            response = self.client.post(
                url_for("customer.send_sms"), query_string=NEW_DATA
            )
        self.assert200(response)
        self.assertEqual(response.json, self.shared_responses.send_sms())
        self.assertTrue(mock_send_sms.called)
        self.assertEqual(mock_send_sms.call_count, 1)

    @pytest.mark.customer
    def test_notification_service_mail(self):
        with patch("app.services.notification_service.NotificationService"
                   ".send_mail") as mock_send_mail:
            self.client.post(url_for("customer.send_mail"),
                             query_string=NEW_DATA)
        self.assertTrue(mock_send_mail.called)
        self.assertEqual(mock_send_mail.call_count, 1)

    @pytest.mark.customer
    def test_notification_service_sms(self):
        with patch("app.services.notification_service.NotificationService"
                   ".send_sms") as mock_send_sms:
            self.client.post(url_for("customer.send_sms"),
                             query_string=NEW_DATA)
        self.assertTrue(mock_send_sms.called)
        self.assertEqual(mock_send_sms.call_count, 1)


if __name__ == "__main__":
    unittest.main()
