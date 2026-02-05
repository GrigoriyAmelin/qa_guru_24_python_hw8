from enum import Enum


class Status(Enum):
    DRAFT = 'Draft'
    READY = 'Ready'
    SENT = 'Sent'
    FAILED = 'Failed'
    INVALID = 'Invalid'