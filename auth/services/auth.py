from auth.adapters import DjangoCredentialRepository
from auth.usecases import CreateCredential
from auth.usecases.exceptions import CredentialAlreadyExists


class AuthService:

    def create_credential(self, username: str, password: str) -> (list, dict):
        errors = list()
        credential_data = dict()
        repository = DjangoCredentialRepository()

        try:
            usecase = CreateCredential(repository, username, password)
            new_credential = usecase.execute()
        except (CredentialAlreadyExists, ValueError) as ex:
            errors.append(str(ex))
        else:
            credential_data.update({
                'username': new_credential.username,
                'uuid': new_credential.uuid,
            })

        return errors, credential_data
