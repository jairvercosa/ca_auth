import pytest

from uuid import uuid4

from django_mock_queries.query import MockSet

from auth.entities import Credential

from auth.adapters import DjangoCredentialRepository
from auth.adapters.django_credential_repository import UserAccount


UUID_MOCK = uuid4()


@pytest.fixture
def mock_set(mocker):
    mockset = MockSet(
        UserAccount(
            uuid=UUID_MOCK,
            username='john.smith',
            password='P@ssw0rd'
        ),
        UserAccount(
            uuid=uuid4(),
            username='john.smith2',
            password='P@ssw0rd'
        )
    )
    mocker.patch.object(UserAccount, 'objects', mockset)


class TestFind:

    def test_when_credential_matches_returns_a_credential(self, mock_set):
        instance = DjangoCredentialRepository()
        credential = instance.find(UUID_MOCK)

        assert isinstance(credential, Credential)

    def test_when_credential_does_not_match_returns_none(self, mock_set):
        instance = DjangoCredentialRepository()
        result = instance.find(uuid4())

        assert result is None


class TestFindBy:

    def test_when_credential_matches_returns_a_credential(self, mock_set):
        instance = DjangoCredentialRepository()
        credential = instance.find_by('john.smith2')

        assert isinstance(credential, Credential)

    def test_when_credential_does_not_match_returns_none(self, mock_set):
        instance = DjangoCredentialRepository()
        result = instance.find_by('test')

        assert result is None


class TestCreate:

    def test_persist_user_account(self, mocker):
        create_user = mocker.patch.object(UserAccount.objects, 'create_user')
        instance = DjangoCredentialRepository()
        instance.create(Credential(
            'john.smith4',
            'P@ssw0rd'
        ))

        assert create_user.called is True

    def test_return_credential(self, mocker):
        user = UserAccount(username='john.smith5', password='P@ssw0rd')
        mocker.patch.object(UserAccount.objects, 'create_user', return_value=user)

        instance = DjangoCredentialRepository()
        new_credential = instance.create(Credential(user.username, user.password))

        assert isinstance(new_credential, Credential)


@pytest.fixture
def update_user(mocker):
    mockset = MockSet(
        UserAccount(
            uuid=UUID_MOCK,
            username='john.smith',
            password='P@ssw0rd'
        )
    )
    mocker.patch.object(UserAccount, 'objects', mockset)
    return mocker.patch.object(UserAccount, 'save')


class TestUpdateStatus:

    def test_persist_user_account(self, update_user):
        instance = DjangoCredentialRepository()
        instance.update_status(Credential(
            'john.smith4',
            'P@ssw0rd',
            uuid=UUID_MOCK
        ))

        assert update_user.called is True

    def test_update_active_attribute(self, update_user):
        instance = DjangoCredentialRepository()

        credential = Credential('john.smith', 'P@ssw0rd', uuid=UUID_MOCK)
        credential.deactivate()

        credential = instance.update_status(credential)

        assert credential.active is False


class TestUpdatePassword:

    def test_persist_user_account(self, update_user):
        instance = DjangoCredentialRepository()
        instance.update_password(Credential(
            'john.smith4',
            'P@ssw0rd',
            uuid=UUID_MOCK
        ))

        assert update_user.called is True

    def test_update_password(self, update_user):
        instance = DjangoCredentialRepository()

        credential = Credential('john.smith', uuid=UUID_MOCK)
        credential.set_password('P@ssw0rd')
        credential = instance.update_password(credential)

        assert bool(credential.password) is True
