from django.urls import path

from .views import CreateCredentialView


urlpatterns = [
    path('register/', CreateCredentialView.as_view(), name='register'),
]
