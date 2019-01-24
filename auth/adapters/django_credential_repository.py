from django.core.exceptions import ObjectDoesNotExist

from identity.account.models import UserAccount
from auth.entities import Credential

from .interfaces import CredentialRepositoryInterface


class DjangoCredentialRepository(CredentialRepositoryInterface):

    def find(self, uuid):
        user = self._find_user_account({'uuid': uuid})
        return self._factory_credential(user)

    def find_by(self, username):
        user = self._find_user_account({'username': username})
        return self._factory_credential(user)

    def create(self, credential):
        user = UserAccount.objects.create_user(
            credential.username,
            credential.password
        )
        return self._factory_credential(user)

    def update_status(self, credential):
        user = self._find_user_account({'uuid': credential.uuid})
        user.is_active = credential.active
        user.save()

        return self._factory_credential(user)

    def update_password(self, credential):
        user = self._find_user_account({'uuid': credential.uuid})
        user.password = credential.password
        user.save()

        return self._factory_credential(user)

    def _factory_credential(self, user):
        if user:
            return Credential(
                user.username,
                user.password,
                uuid=user.uuid,
                active=user.is_active
            )

    def _find_user_account(self, params):
        try:
            user = UserAccount.objects.get(**params)
        except ObjectDoesNotExist:
            return None
        else:
            return user
