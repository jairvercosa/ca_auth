import pytest

from adapters import CredentialRepositoryInterface
from entities import Credential

from usecases import CreateCredential
from usecases.exceptions import CredentialAlreadyExists


class EmptyRepository(CredentialRepositoryInterface):

    def find(self):
        pass

    def find_by(self, username):
        pass

    def create(self, credential):
        return credential

    def update_status(self, credential):
        pass

    def update_password(self, credential):
        pass


class Repository(EmptyRepository):

    def find_by(self, username):
        return Credential(username, 'P@ssw0rd')


@pytest.fixture
def get_instance():
    return CreateCredential(
        EmptyRepository(),
        'john.smith',
        'P@ssw0rd'
    )


class TestInit:

    def test_initialize(self, get_instance):
        instance = get_instance
        assert bool(instance) is True

    def test_inicialize_repository(self, get_instance):
        instance = get_instance
        assert isinstance(instance.repository, CredentialRepositoryInterface)

    def test_when_username_is_not_provieded_raise_exception(self):
        with pytest.raises(ValueError):
            CreateCredential(Repository(), '', 'Password')

    def test_when_password_is_not_provided_raise_exception(self):
        with pytest.raises(ValueError):
            CreateCredential(Repository(), 'john.smith', '')


class TestExceute:

    def test_when_username_already_exists_raise_exception(self):
        with pytest.raises(CredentialAlreadyExists):
            instance = CreateCredential(
                Repository(),
                'john.smith',
                'P@ssw0rd'
            )

            instance.execute()

    def test_when_username_does_not_exists_persists_the_data(self, get_instance, mocker):
        instance = get_instance

        EmptyRepository.create = mocker.MagicMock(
            return_value=Credential('smith')
        )

        instance.execute()
        assert EmptyRepository.create.called

    def test_when_username_does_not_exists_return_a_credential(self, get_instance):
        instance = get_instance
        new_credential = instance.execute()

        assert isinstance(new_credential, Credential)
