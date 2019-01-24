from auth.entities import Credential
from auth.adapters import CredentialRepositoryInterface

from .interfaces import UseCaseInterface
from .exceptions import CredentialAlreadyExists


class CreateCredential(UseCaseInterface):

    def __init__(
        self,
        repository: CredentialRepositoryInterface,
        username: str,
        password: str
    ):
        self.__repository = repository

        if not password:
            raise ValueError('Username or password not provided.')

        self.__username = username
        self.__password = password

    @property
    def repository(self) -> CredentialRepositoryInterface:
        return self.__repository

    def execute(self) -> Credential:
        if self.__repository.find_by(self.__username):
            raise CredentialAlreadyExists('Credential already exists')

        credential = self._factory_credential()
        return self.__repository.create(credential)

    def _factory_credential(self) -> Credential:
        instance = Credential(self.__username)
        instance.set_password(self.__password)
        return instance
