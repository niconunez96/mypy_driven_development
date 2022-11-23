import abc

from src.protocol_vs_abc.types import EmailMessage, EmailUnsent, Failure


class EmailSender(abc.ABC):
    @abc.abstractmethod
    def send_email(self, message: EmailMessage) -> None | Failure:
        raise NotImplementedError

    @abc.abstractmethod
    def send_bulk(self, messages: list[EmailMessage]) -> None | list[EmailUnsent]:
        raise NotImplementedError


class DummyEmailSender(EmailSender):
    # def send_email(self, message: EmailMessage) -> None | Failure:
    #     if "boom" in message["subject"]:
    #         return Failure("Boom 💥 from protocol")
    #     print("Sending email through abstract class...📬")
    #     return None

    def send_bulk(self, messages: list[EmailMessage]) -> None | list[EmailUnsent]:
        results = [self.send_email(message) for message in messages]
        errors = [
            EmailUnsent(message["to"], message, result)
            for message, result in zip(messages, results)
            if isinstance(result, Failure)
        ]
        return None if not errors else errors


"""
Mypy complains ❌ at instantiation level when we have an incomplete concrete class.
Mypy don't complain at reference level because it assumes that the concrete class
has already implement the abstract methods
"""
dummy_email_sender = DummyEmailSender()
