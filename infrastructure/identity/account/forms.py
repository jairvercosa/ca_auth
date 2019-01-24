from django import forms


class RegisterCredentialForm(forms.Form):

    username = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput()
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if confirm_password != password:
            raise forms.ValidationError(
                'Password and confirmation do not match each other'
            )

        return confirm_password
