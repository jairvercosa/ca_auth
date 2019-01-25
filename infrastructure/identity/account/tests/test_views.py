from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from identity.account.views import (
    AuthService,
    CreateCredentialView,
    FormView,
)


class TestFormValid:

    def test_execute_create_credential_service_method(self, mocker):
        mocker.patch('identity.account.views.HttpResponse')
        mocker.patch.object(
            AuthService,
            'create_credential',
            return_value=(None, {})
        )
        mocker.patch.object(FormView, 'form_valid', return_value=None)

        view = CreateCredentialView()
        view.request = mocker.Mock()

        form_class = view.get_form_class()
        form = form_class(data={
            'username': 'johnsmith',
            'password': 'P@ssword99',
            'confirm_password': 'P@ssword99',
        })
        form.is_valid()

        view.form_valid(form)
        assert AuthService.create_credential.called is True

    def test_when_form_is_valid_and_auth_service_has_error_return_error(
        self,
        mocker
    ):
        mocker.patch.object(
            AuthService,
            'create_credential',
            return_value=(['Error'], {})
        )
        mocker.patch.object(
            CreateCredentialView,
            'form_invalid',
            return_value=None
        )

        view = CreateCredentialView()
        form_class = view.get_form_class()
        form = form_class(data={
            'username': 'johnsmith',
            'password': 'password',
            'confirm_password': 'password',
        })
        form.is_valid()

        view.form_valid(form)
        assert CreateCredentialView.form_invalid.called is True


class TestRequest:

    def test_when_send_a_get_request_return_200(self):
        factory = RequestFactory()
        request = factory.get('/account/register/')
        request.user = AnonymousUser()

        response = CreateCredentialView.as_view()(request)
        assert response.status_code == 200
