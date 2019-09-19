# -*- coding: utf-8 -*-
"""
To hold application specific code.

Created to override the default AppConfig to check for NotificationType model
creation.
"""
from django.apps import AppConfig, apps
from django.conf import settings

from api.contents import project_invitation_email_template, \
    registration_email_template, forgot_password_email_template


class ApiConfig(AppConfig):
    """Runs at django start."""

    name = 'api'

    def ready(self):
        """
        To execute on app load.

        Creates Notification types specified in settings missing in database
        Checking implementation of basic abstract methods
        """
        super().ready()
        notification_type_model = apps.get_model('api', 'NotificationType')
        notification_template_model = apps.get_model('api',
                                                     'NotificationTemplate')
        notification_types_in_db = set(
            notification_type_model.objects.values_list('code', flat=True),
        )
        notification_types_from_settings = {
            item['code'].lower() for item in settings.NOTIFICATIONS_SETTINGS
        }
        for to_create in (
                notification_types_from_settings - notification_types_in_db
        ):
            notification_type_model.objects.create(code=to_create)

        project_invitation, \
        created = notification_template_model.objects.get_or_create(
            name="project_invitation")
        if created:
            project_invitation.content = project_invitation_email_template
            project_invitation.save()
        registration, \
        created = notification_template_model.objects.get_or_create(
            name="registration")
        if created:
            registration.content = registration_email_template
            registration.save()

        forgot_password, \
        created = notification_template_model.objects.get_or_create(
            name="forgot_password")
        if created:
            forgot_password.content = forgot_password_email_template
            forgot_password.save()
