from usecases import CreateCredential
from usecases.exceptions import CredentialAlreadyExists
from adapters import DjangoCredentialRepository


class AuthService:

    def create_credential(self, username, password):
        errors = list()
        credential_data = dict()
        repository = DjangoCredentialRepository()

        try:
            usecase = CreateCredential(repository, username, password)
            new_credential = usecase.execute()
        except ValueError as ex:
            errors.append(str(ex))
        except CredentialAlreadyExists as ex:
            errors.append(str(ex))
        else:
            credential_data['username'] = new_credential.username
            credential_data['uuid'] = new_credential.uuid

        return errors, credential_data
