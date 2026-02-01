from dataclasses import dataclass, field
from typing import Optional

from src.email_address import EmailAddress
from src.status import Status


@dataclass
class Email:
    subject: str
    body: str
    sender: EmailAddress
    recipients: EmailAddress | list[EmailAddress]
    date: Optional[str]
    short_body: Optional[str]
    status: Status = field(default=Status.DRAFT)

    @property
    def email_recipient_list(self):
        list_of_recipients = []
        for recipient in self.recipients:
            list_of_recipients.append(recipient.email_address)
        return list_of_recipients


    def __post_init__(self):
        if isinstance(self.recipients, EmailAddress):
            self.recipients = [self.recipients]

    def clean_text_fields(self, field: str) -> str:
        return (field.replace("\n", "").replace("\t", " ").replace("  ", " "))

    def check_empty_fields(self) -> bool:
        return bool(self.subject.strip()) and bool(self.body.strip()) \
            and bool(self.sender.email_address.strip()) and bool(self.recipients)


    def add_short_body(self) -> str:
        return self.body[0:20]+"..."

    def prepare(self):
        self.subject = self.clean_text_fields(self.subject)
        self.body = self.clean_text_fields(self.body)
        if self.check_empty_fields():
            self.status = Status.READY
        else: self.status = Status.INVALID
        self.short_body = self.add_short_body()

    def __repr__(self) ->str:
        return (f"(\n"
                f"subject='{self.subject}',\n"
                f"body='{self.body}',\n"
                f"sender='{self.sender.masked}',\n"
                f"recipients='{self.email_recipient_list}',\n"
                f"date='{self.date}',\n"
                f"short_body='{self.short_body}',\n"
                f"status='{self.status.value}'\n)"
                )