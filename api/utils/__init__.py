from django.conf import settings
from django.utils.module_loading import import_string


def get_notification_type_handler(code):
    """
    :param code: looks for `module` key according to matching `code`
    in settings.NOTIFICATIONS_SETTINGS and returns the instance `object()` of the module
    :return: api.utils.notification.type.ClassName()
    """
    project_settings = settings.NOTIFICATIONS_SETTINGS
    for index, item in enumerate(project_settings):
        if item['code'].lower() == code:
            relative_path = item['module']
            return import_string(relative_path)()
