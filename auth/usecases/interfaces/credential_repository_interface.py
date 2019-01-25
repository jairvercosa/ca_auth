import abc

from auth.entities import CredentialInterface


class CredentialRepositoryInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def find(self, uuid: 'UUID') -> CredentialInterface:
        pass

    @abc.abstractmethod
    def find_by(self, username: str) -> CredentialInterface:
        pass

    @abc.abstractmethod
    def create(self, credential: str) -> CredentialInterface:
        pass

    @abc.abstractmethod
    def update_status(self, credential: str) -> CredentialInterface:
        pass

    @abc.abstractmethod
    def update_password(self, credential: str) -> CredentialInterface:
        pass
