from abc import ABC, abstractmethod
from typing import Mapping, List

from django.core.mail import EmailMessage

DEFAULT_SENDER = 'noreply@satakuntalainenosakunta.fi'


class AbstractEmailService(ABC):
    @abstractmethod
    def send(self, fields: Mapping[str, object], reply_to: str = None):
        pass


class EmailService(AbstractEmailService):
    def __init__(self,
                 subject: str,
                 from_email: str,
                 to_email: List[str]):
        self.subject = subject
        self.from_email = from_email
        self.to_email = to_email

    def send(self, fields: Mapping[str, object], reply_to: str = None):
        EmailMessage(
            subject=self.subject,
            body=self._construct_message(fields),
            from_email=self.from_email,
            to=self.to_email,
            reply_to=[reply_to or DEFAULT_SENDER],
        ).send()

    @staticmethod
    def _construct_message(data: Mapping[str, object]) -> str:
        return '\n\n'.join(f'{k}:\n{v}' for k, v in data.items())
