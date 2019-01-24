from .interfaces import CredentialRepositoryInterface


class DjangoCredentialRepository(CredentialRepositoryInterface):

    def find(self, uuid):
        pass

    def find_by(self, username):
        pass

    def create(self, credential):
        pass

    def update_status(self, credential):
        pass

    def update_password(self, credential):
        pass
