import abc


class CredentialRepositoryInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def find(self, uuid):
        pass

    @abc.abstractmethod
    def find_by(self, username):
        pass

    @abc.abstractmethod
    def create(self, credential):
        pass

    @abc.abstractmethod
    def update_status(self, credential):
        pass

    @abc.abstractmethod
    def update_password(self, credential):
        pass
