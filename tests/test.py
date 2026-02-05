from src.email import Email
from src.email_address import EmailAddress
from src.email_service import EmailService
from src.status import Status


def test_send_single_email_one():
    email = Email(subject='Subject',
                body='Hi, this is me',
                sender=EmailAddress('wre@12.ru'),
                recipients=[EmailAddress('tre@.oup.com')],
                date='12-23-23',
                short_body='dfgg ERYR fgfdg ...',
                status=Status.FAILED)
    service = EmailService(email)
    result = service.send_email()
    for res in result:
        print(f'\n{res}')

    assert len(result) == 1
    assert result[0].status == Status.FAILED


def test_send_single_email_two():
    email = Email(subject='Subject',
                body='Hi, this is me',
                sender=EmailAddress('wre@12.ru'),
                recipients=EmailAddress('tre@.oup.com'),
                date='12-01-23',
                short_body='dfgg ERYR fgfdg ...',
                status=Status.DRAFT)
    service = EmailService(email)
    result = service.send_email()
    for res in result:
        print(f'\n{res}')

    assert len(result) == 1
    assert result[0].status == Status.FAILED


def test_with_prepare_send_multiple_email():
    email = Email(subject='Subject',
                body='Hi, this is me, such an incredible person!',
                sender=EmailAddress('wre@12.ru'),
                recipients=[EmailAddress('tre@.oup.com'), EmailAddress('ertt@poison2.net ')],
                date='12-23-23',
                short_body='dfgg ERYR fgfdg ...',
                status=Status.FAILED)

    email.prepare()
    service = EmailService(email)
    result = service.send_email()
    for res in result:
        print(f'\n{res}')

    assert len(result) == 2
    assert result[0].status == Status.SENT


def test_with_prepare_send_email():
    email = Email(subject='Subject',
                body='Hi, this is me, such an incredible person!',
                sender=EmailAddress('wre@12.ru'),
                recipients=[EmailAddress('tre@.oup.com'), EmailAddress('ertt@poison.net')],
                date='12-23-23',
                short_body='dfgg ERYR fgfdg ...',
                status=Status.FAILED)

    email.prepare()
    service = EmailService(email)
    result = service.send_email()
    for res in result:
        print(f'\n{res}')

    assert len(result) == 2
    assert result[1].status == Status.SENT
    assert '...' in result[0].short_body