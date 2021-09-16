from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
  url(r'^$', views.index, name='index'),
  url('accounts/register', views.register_new_user, name='register'),
  # url('accounts', include('django.contrib.auth.urls')),
  ]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)