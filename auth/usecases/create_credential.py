from auth.entities import Credential

from .interfaces import UseCaseInterface
from .exceptions import CredentialAlreadyExists


class CreateCredential(UseCaseInterface):

    def __init__(self, repository, username, password):
        self.__repository = repository

        if not password:
            raise ValueError('Username or password not provided.')

        self.__username = username
        self.__password = password

    @property
    def repository(self):
        return self.__repository

    def execute(self):
        if self.__repository.find_by(self.__username):
            raise CredentialAlreadyExists('Credential already exists')

        credential = self._factory_credential()
        return self.__repository.create(credential)

    def _factory_credential(self):
        instance = Credential(self.__username)
        instance.set_password(self.__password)
        return instance
