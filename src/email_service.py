import copy
import datetime

from src.email import Email
from src.status import Status


class EmailService:
    def __init__(self, email: Email):
        self.email = email


    @staticmethod
    def add_send_date() -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d")


    def send_email(self) -> list:
        recipients_mails = []
        for recipient in self.email.recipients:
            edc = copy.deepcopy(self.email)
            edc.date = self.add_send_date()
            edc.recipients = [recipient]
            if edc.status == Status.READY:
                edc.status = Status.SENT
            else:
                edc.status = Status.FAILED
            recipients_mails.append(edc)
        return recipients_mails