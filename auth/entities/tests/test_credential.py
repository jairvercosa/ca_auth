import pytest

from uuid import uuid4, UUID

from entities import Credential
from entities.values import Password


@pytest.fixture
def get_instance():
    return Credential('john.smith')


class TestInit:

    def test_initialize(self, get_instance):
        instance = get_instance
        assert bool(instance) is True

    def test_when_uuid_is_provided_set_credential_uuid(self):
        expected_result = uuid4()
        instance = Credential('john.smith', uuid=expected_result)

        assert instance.uuid == expected_result

    def test_when_uuid_not_provided_set_a_new_one(self, get_instance):
        instance = get_instance
        assert isinstance(instance.uuid, UUID)

    def test_when_username_is_provided_set_credential_username(self, get_instance):
        expected_result = 'john.smith'

        instance = get_instance
        assert instance.username == expected_result

    def test_when_username_is_not_provided_raise_exception(self):
        with pytest.raises(ValueError):
            Credential(None)

    def test_when_active_is_not_provided_set_credential_active_to_true(self, get_instance):
        expected_result = True

        instance = get_instance
        assert instance.active == expected_result

    def test_when_active_is_provided_set_credential_active(self):
        expected_result = False

        instance = Credential('john.smith', active=expected_result)
        assert instance.active == expected_result

    def test_when_password_is_provided_set_credential_password(self):
        instance = Credential('john.smith', 'P@ssw0rd')
        assert isinstance(instance.password, Password)


class TestUsernameSetter:

    def test_when_username_id_not_provided_raise_exception(self, get_instance):
        with pytest.raises(ValueError):
            instance = get_instance
            instance.username = None

    def test_when_username_is_provided(self, get_instance):
        expected_result = 'Marco.Nunes'

        instance = get_instance
        instance.username = 'Marco.Nunes'
        assert instance.username == expected_result


class TestSetPassword:

    def test_when_password_is_not_provided_raise_exception(self, get_instance):
        with pytest.raises(ValueError):
            instance = get_instance
            instance.set_password(None)

    def test_when_password_is_provided_set_new_password(self, get_instance):
        instance = get_instance
        instance.set_password('P@ssw0rd')

        assert bool(instance.password) is True


class TestVerify:

    def test_when_password_is_not_equal_returns_false(self, get_instance):
        instance = get_instance
        instance.set_password('P@ssw0rd')
        assert instance.verify('Password') is False

    def test_when_password_is_equal_returns_true(self, get_instance):
        password_value = 'P@ssw0rd'
        instance = get_instance
        instance.set_password(password_value)
        assert instance.verify(password_value) is True


class TestDeactivate:

    def test_set_active_to_false(self, get_instance):
        instance = get_instance
        instance.deactivate()
        assert instance.active is False
