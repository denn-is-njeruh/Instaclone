from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  url('accounts/', include('django_registration.backends.one_step.urls')),
  url('accounts', include('django.contrib.auth.urls')),
  ]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)