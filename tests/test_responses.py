from datetime import date, time


class SharedResponse:
    def send_sms(self):
        return {"status": "sms sent"}

    def send_mail(self):
        return {"status": "email sent"}