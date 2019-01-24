from django.views.generic import FormView
from django.urls import reverse_lazy

from auth.services import AuthService

from .forms import RegisterCredentialForm


class CreateCredentialView(FormView):
    template_name = 'register.html'
    form_class = RegisterCredentialForm
    success_url = reverse_lazy('summary')

    def form_valid(self, form):
        service = AuthService()
        errors, credential = service.create_credential(
            form.data['username'],
            form.data['password']
        )

        if errors:
            for error_msg in errors:
                form.add_error(None, error_msg)

            return self.form_invalid(form)

        return super().form_valid(form)
