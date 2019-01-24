import abc


class CredentialInterface(metaclass=abc.ABCMeta):

    @abc.abstractproperty
    def uuid(self):
        pass

    @abc.abstractproperty
    def username(self):
        pass

    @abc.abstractproperty
    def password(self):
        pass

    @abc.abstractproperty
    def active(self):
        pass

    @abc.abstractmethod
    def set_password(self):
        pass

    @abc.abstractmethod
    def verify(self):
        pass

    @abc.abstractmethod
    def deactivate(self):
        pass
