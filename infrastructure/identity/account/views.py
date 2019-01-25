from django.http import HttpResponse
from django.template import loader
from django.views.generic import FormView

from auth.services import AuthService

from .forms import RegisterCredentialForm


class CreateCredentialView(FormView):
    template_name = 'register.html'
    success_template_name = 'success_registry.html'
    form_class = RegisterCredentialForm

    def form_valid(self, form):
        errors, _ = self._perform_operation(form)

        if errors:
            for error_msg in errors:
                form.add_error(None, error_msg)

            return self.form_invalid(form)

        return self._get_success_response()

    def _perform_operation(self, form):
        service = AuthService()
        return service.create_credential(
            form.data['username'],
            form.data['password']
        )

    def _get_success_response(self):
        template = loader.get_template(self.success_template_name)
        return HttpResponse(template.render({}, self.request))
