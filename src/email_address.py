class EmailAddress:

    def __init__(self, email_address: str):
        self._email_address: str = self.normalize_address(email_address)
        if not self.validate_address(self._email_address):
            raise ValueError(f'Email address {self._email_address} is no valid')

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value

    @property
    def masked(self):
        login, domain = self._email_address.split('@')
        return login[:2] + '***@' + domain

    @staticmethod
    def normalize_address(email_address: str) -> str:
        return email_address.lower().strip()

    def validate_address(self, _email_address: str) -> bool:
        extentions = ('.ru', '.com', '.net')
        return self.email_address.endswith(extentions) and "@" in self.email_address