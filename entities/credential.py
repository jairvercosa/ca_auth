from uuid import uuid4

from .interfaces import CredentialInterface
from .values import Password


class Credential(CredentialInterface):

    def __init__(self, username, password=None, active=True, uuid=None):
        self.__uuid = uuid or uuid4()

        self.__password = Password(password)
        self.__active = active

        self.username = username

    @property
    def uuid(self):
        return self.__uuid

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value is None:
            raise ValueError('Username cannot be null.')

        self.__username = value

    @property
    def password(self):
        return self.__password

    @property
    def active(self):
        return self.__active

    def set_password(self, value):
        if value is None:
            raise ValueError('Password cannot be null.')

        self.__password = Password(value)

    def verify(self, password):
        return self.__password == password

    def deactivate(self):
        self.__active = False
