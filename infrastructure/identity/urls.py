from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('account/', include('identity.account.urls')),
    path('admin/', admin.site.urls),
]
