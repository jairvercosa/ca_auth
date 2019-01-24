import abc


class CredentialInterface(metaclass=abc.ABCMeta):

    @abc.abstractproperty
    def uuid(self):
        pass

    @abc.abstractproperty
    def username(self) -> str:
        pass

    @abc.abstractproperty
    def password(self) -> 'Password':
        pass

    @abc.abstractproperty
    def active(self) -> bool:
        pass

    @abc.abstractmethod
    def set_password(self, value: str):
        pass

    @abc.abstractmethod
    def verify(self, password: str) -> bool:
        pass

    @abc.abstractmethod
    def deactivate(self):
        pass
