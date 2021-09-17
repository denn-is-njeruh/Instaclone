from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PhiimagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phiimages'

    def ready(self):
        import phiimages.signals 




