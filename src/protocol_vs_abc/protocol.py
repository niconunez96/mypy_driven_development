from typing import Protocol

from src.protocol_vs_abc.types import EmailMessage, EmailUnsent, Failure


class EmailSender(Protocol):
    def send_email(self, message: EmailMessage) -> None | Failure:
        raise NotImplementedError

    def send_bulk(self, messages: list[EmailMessage]) -> None | list[EmailUnsent]:
        raise NotImplementedError


class DummyEmailSender:
    def send_email(self, message: EmailMessage) -> None | Failure:
        if "boom" in message["subject"]:
            return Failure("Boom 💥 from protocol")
        print("Sending email through protocols...📬")
        return None

    # def send_bulk(self, messages: list[EmailMessage]) -> None | list[EmailUnsent]:
    #     results = [self.send_email(message) for message in messages]
    #     errors = [
    #         EmailUnsent(message["to"], message, result)
    #         for message, result in zip(messages, results)
    #         if isinstance(result, Failure)
    #     ]
    #     return None if not errors else errors


"""
Mypy don't complain ✅ at instantiation level when we have an incomplete concrete class.
This is because we don't need inheritance/implementation with Protocols.
Protocols are meant for clients, if a client request an API of the form of 'EmailSender',
then any object that fulfills that contract will pass the mypy check.
Its name is 'static duck typing'.
"""
dummy_email_sender = DummyEmailSender()
