# from app.utils.task_scheduler import send_mail, send_sms


class NotificationService:
    def send_mail(self, email_info: dict):
        from app.utils.task_scheduler import send_mail
        send_mail.delay(email_info)

    def send_sms(self, sms_info: dict):
        from app.utils.task_scheduler import send_sms
        send_sms.delay(sms_info)
