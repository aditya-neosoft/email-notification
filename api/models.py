from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from api.choices import NOTIFICATION_TYPE_CHOICES
from api.utils.validators import JSONValidator
from api.utils import get_notification_type_handler


class NotificationType(models.Model):
    """
        model for notification type like code : sms,email,push etc.
     """
    code = models.CharField(max_length=40, unique=True, choices=NOTIFICATION_TYPE_CHOICES)


class NotificationTemplate(models.Model):
    """
       model for template format for the notification
    """
    content = models.TextField(blank=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Notification(models.Model):
    """
        model for notification to send with scheduled time,predefined template,receiver email or phonenumber etc.
    """
    template = models.ForeignKey(NotificationTemplate,
                                 on_delete=models.CASCADE,
                                 related_name='templates')
    context = models.TextField(default='{}', validators=[JSONValidator()])
    created_at = models.DateTimeField(_('created at'), default=timezone.now)
    type = models.ForeignKey(NotificationType, on_delete=models.CASCADE,
                             related_name='notifications')
    receiver = models.CharField(max_length=50, blank=False, null=False)
    is_sent = models.BooleanField(default=False)
    send_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        """
        relevant validations depending type and receiver
        :return: None or raises ValidationError
        """
        notification_type_handler = get_notification_type_handler(self.type.code.lower())
        notification_type_handler.validate(self.receiver)
        super().clean()
