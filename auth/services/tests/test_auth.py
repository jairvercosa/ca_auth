import pytest

from uuid import UUID

from entities import Credential
from services import AuthService
from services.auth import DjangoCredentialRepository


@pytest.fixture
def create_credential_response(mocker):
    credential = Credential('john.smith', 'P@ssw0rd')

    mocker.patch.object(
        DjangoCredentialRepository,
        'create',
        return_value=credential
    )

    instance = AuthService()
    return instance.create_credential('john.smith', 'P@ssw0rd')


class TestCreateCredential:

    def test_returns_a_tuple(self, create_credential_response):
        assert isinstance(create_credential_response, tuple)

    def test_when_success_returns_empty_list_for_errors(self, create_credential_response):
        errors, _ = create_credential_response
        assert bool(errors) is False

    def test_returns_a_dict_with_username(self, create_credential_response):
        expected_result = 'john.smith'
        _, credential = create_credential_response

        assert credential.get('username') == expected_result

    def test_returns_a_dict_with_uuid(self, create_credential_response):
        _, credential = create_credential_response

        assert isinstance(credential.get('uuid'), UUID)

    def test_when_error_returns_a_list_with_errors(self, mocker):
        instance = AuthService()
        errors, _ = instance.create_credential('john.smith', None)
        assert bool(errors) is True
