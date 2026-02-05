from dataclasses import dataclass, field
from time import sleep
from typing import Optional

from src.email_address import EmailAddress
from src.status import Status


@dataclass
class Email:
    subject: str
    body: str
    sender: EmailAddress
    recipients: EmailAddress | list[EmailAddress]
    date: Optional[str] = field(default=None)
    short_body: Optional[str] = field(default=None)
    status: Status = field(default=Status.DRAFT)


    def __post_init__(self):
        if isinstance(self.recipients, EmailAddress):
            self.recipients = [self.recipients]


    def get_recipients_str(self) -> str:
        list_of_recipients = []
        for recipient in self.recipients:
            list_of_recipients.append(recipient.email_address)
        return ', '.join(list_of_recipients)


    def clean_data(self):
        self.subject = " ".join(self.subject.split())
        self.body = " ".join(self.body.split())
        return self


    def check_empty_fields(self) -> bool:
        return bool(self.subject.strip()) and bool(self.body.strip()) \
            and bool(self.sender.email_address.strip()) and bool(self.recipients)


    def add_short_body(self, n=10):
        if not len(self.body):
            return self
        if len(self.body) > n:
            self.short_body = self.body[0:n]+"..."
        else:
            self.short_body = self.body
        return self


    def prepare(self):
        self.clean_data()
        if self.check_empty_fields():
            self.status = Status.READY
        else: self.status = Status.INVALID
        self.add_short_body()


    def __repr__(self) -> str:
        return (f"\n"                
                f"Статус: '{self.status.value}'\n"
                f"Кому: '{self.get_recipients_str()}',\n"
                f"От: '{self.sender.masked}',\n"
                f"Тема: '{self.subject}',\n"
                f"Дата: '{self.date}',\n"
                f"Письмо: '{self.short_body if self.short_body else self.body}'\n"
                )