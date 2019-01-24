from uuid import uuid4, UUID

from .interfaces import CredentialInterface
from .values import Password


class Credential(CredentialInterface):

    def __init__(
        self,
        username: str,
        password: str=None,
        active: bool=True,
        uuid: UUID=None
    ):
        self.__uuid = uuid or uuid4()

        self.__password = Password(password)
        self.__active = active

        self.username = username

    @property
    def uuid(self) -> UUID:
        return self.__uuid

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str):
        if value is None:
            raise ValueError('Username cannot be null.')

        self.__username = value

    @property
    def password(self) -> Password:
        return self.__password

    @property
    def active(self) -> bool:
        return self.__active

    def set_password(self, value: str):
        if value is None:
            raise ValueError('Password cannot be null.')

        self.__password.value = value

    def verify(self, password: str) -> bool:
        return self.__password == password

    def deactivate(self):
        self.__active = False
