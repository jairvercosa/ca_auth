import abc


class EncryptorInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def encrypt(cls, value):
        pass

    @abc.abstractmethod
    def verify(cls, value, encrypted):
        pass
