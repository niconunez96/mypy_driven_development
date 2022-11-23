from datetime import datetime, timedelta
from typing import Optional

from typing_extensions import assert_never

from src.protocol_vs_abc.abstract_class import EmailSender as EmailSenderABC
from src.protocol_vs_abc.protocol import EmailSender as EmailSenderProtocol
from src.protocol_vs_abc.types import EmailMessage, Failure


def fetch_lasts_scheduled_email(user_id: str) -> list[EmailMessage]:
    return [
        {"to": ["pepito@email.com"], "subject": "test", "body": "something"},
        {"to": ["pepito@email.com", "boom@email.com"], "subject": "boom", "body": "something"},
    ]


def fetch_last_scheduled_email(user_id: str) -> Optional[EmailMessage]:
    return {"to": ["pepito@email.com"], "subject": "test", "body": "something"}


def retry(email_message: EmailMessage, when: timedelta) -> None:
    print(f"Retrying {email_message} at {datetime.now() + when} 🔄")


def send_email_protocol(user_id: str, email_sender: EmailSenderProtocol) -> None:
    email_message = fetch_last_scheduled_email(user_id)
    if not email_message:
        print("No email message to send")
        return
    result = email_sender.send_email(email_message)
    match (result):
        case None:
            print("Email has been sent successfully")
        case Failure(error_message):
            print(error_message)
            retry(email_message, timedelta(minutes=10))
        case _:
            assert_never(result)


def send_email_abc(user_id: str, email_sender: EmailSenderABC) -> None:
    email_message = fetch_last_scheduled_email(user_id)
    if not email_message:
        print("No email message to send")
        return
    result = email_sender.send_email(email_message)
    match (result):
        case None:
            print("Email has been sent successfully")
        case Failure(error_message):
            print(error_message)
            retry(email_message, timedelta(minutes=10))
        case _:
            assert_never(result)


def send_emails_protocol(user_id: str, email_sender: EmailSenderProtocol) -> None:
    email_messages = fetch_lasts_scheduled_email(user_id)
    if not email_messages:
        print("No email message to send")
        return
    result = email_sender.send_bulk(email_messages)
    match (result):
        case None:
            print("Email has been sent successfully ✅")
        case list() as emails_unsent:
            for email_unsent in emails_unsent:
                print(email_unsent.failure)
                retry(email_unsent.message, timedelta(minutes=10))
        case _:
            assert_never(result)


def send_emails_abc(user_id: str, email_sender: EmailSenderABC) -> None:
    email_messages = fetch_lasts_scheduled_email(user_id)
    if not email_messages:
        print("No email message to send")
        return
    result = email_sender.send_bulk(email_messages)
    match (result):
        case None:
            print("Email has been sent successfully ✅")
        case list() as emails_unsent:
            for email_unsent in emails_unsent:
                print(email_unsent.failure)
                retry(email_unsent.message, timedelta(minutes=10))
        case _:
            assert_never(result)


def main() -> None:
    from .abstract_class import dummy_email_sender as dummy_email_sender_abc_ex
    from .protocol import dummy_email_sender as dummy_email_sender_protocol_ex

    print("***** Abstract example *****")
    """
    Mypy complains ❌ at instantiation level when we have an incomplete concrete class.
    Mypy don't complain ✅ at reference level because it assumes that the concrete class
    has already implement the abstract methods
    """
    send_email_abc("1", dummy_email_sender_abc_ex)
    send_emails_abc("1", dummy_email_sender_abc_ex)
    print()

    print("***** Protocol example *****")
    """
    Mypy don't complain ✅ at instantiation level when we have an incomplete concrete class.
    This is because we don't need inheritance/implementation with Protocols.
    Protocols are meant for clients, if a client request an API of the form of 'EmailSender',
    then any object that fulfills that contract will pass the mypy check.
    Its name is 'static duck typing'.
    """
    send_email_protocol("1", dummy_email_sender_protocol_ex)
    send_emails_protocol("1", dummy_email_sender_protocol_ex)
    print()
