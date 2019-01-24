from identity.account.forms import RegisterCredentialForm


class TestRequired:

    def test_when_username_is_empty_returns_error_with_username(self):
        data = {
            'username': None,
            'password': 'P@ssword99',
            'confirm_password': 'P@ssword99',
        }

        form = RegisterCredentialForm(data=data)
        form.is_valid()
        assert 'username' in form.errors

    def test_when_password_is_empty_returns_error_with_password(self):
        data = {
            'username': 'johnsmith',
            'password': None,
            'confirm_password': 'P@ssword99',
        }

        form = RegisterCredentialForm(data=data)
        form.is_valid()
        assert 'password' in form.errors

    def test_when_confirm_password_is_empty_returns_error_with_confirm_password(self):
        data = {
            'username': 'johnsmith',
            'password': 'P@ssword99',
            'confirm_password': None,
        }

        form = RegisterCredentialForm(data=data)
        form.is_valid()
        assert 'confirm_password' in form.errors

    def test_when_confirm_password_is_different_from_password_returns_error_with_confirm_password(self):
        data = {
            'username': 'johnsmith',
            'password': 'P@ssword99',
            'confirm_password': 'P@ssword91',
        }

        form = RegisterCredentialForm(data=data)
        form.is_valid()
        assert 'confirm_password' in form.errors

    def test_when_all_fields_are_filled_up_and_password_is_equal_to_confirm_password_the_form_is_valid(self):
        password = 'P@ssword99'
        data = {
            'username': 'johnsmith',
            'password': password,
            'confirm_password': password,
        }

        form = RegisterCredentialForm(data=data)
        assert form.is_valid() is True
