import abc

from auth.entities import CredentialInterface


class UseCaseInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self) -> CredentialInterface:
        pass
