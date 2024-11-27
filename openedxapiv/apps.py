"""
openedxapiv Django application initialization.
"""

import logging
from django.apps import AppConfig
from edx_django_utils.plugins import PluginSettings, PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType

log = logging.getLogger(__name__)



class OpenedxapivConfig(AppConfig):
    """
    Configuration for the openedxapiv Django application.
    """

    name = 'openedxapiv'
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^openedxapiv/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        }
    }
    
    def ready(self):
        log.debug("{label} is ready.".format(label=self.label))
