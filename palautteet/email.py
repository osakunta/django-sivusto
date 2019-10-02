from django.core.mail import EmailMessage

DEFAULT_SENDER = 'noreply@satakuntalainenosakunta.fi'


class EmailService:
    def __init__(self,
                 subject: str,
                 from_email: str,
                 to_email: str):
        self.subject = subject
        self.from_email = from_email
        self.to_email = to_email

    def send(self, message, reply_to: str = None):
        EmailMessage(
            subject=self.subject,
            body=message,
            from_email=self.from_email,
            to=self.to_email,
            reply_to=[reply_to or DEFAULT_SENDER],
        ).send()
