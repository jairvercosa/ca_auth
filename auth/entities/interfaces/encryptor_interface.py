import abc


class EncryptorInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def encrypt(cls, value: str) -> str:
        pass

    @abc.abstractmethod
    def verify(cls, value: str, encrypted: str) -> bool:
        pass
