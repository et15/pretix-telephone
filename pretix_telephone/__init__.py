from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PluginApp(AppConfig):
    name = 'pretix_telephone'
    verbose_name = 'Pretix Phone Number Field'

    class PretixPluginMeta:
        name = gettext_lazy('Pretix Phone Number Field')
        author = 'Felix Rindt'
        description = ugettext_lazy('This plugin adds a contact question asking for the telephone number.')
        visible = True
        version = '2.4.1'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_telephone.PluginApp'
