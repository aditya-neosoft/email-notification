from django.core.management.base import BaseCommand
from django.utils import timezone

from api.models import Notification
from api.utils import get_notification_type_handler


class Command(BaseCommand):
    """
    Fetches and processes notifications that are pending.

    """
    help = 'Fetches and processes notifications that are pending.'

    def handle(self, *args, **kwargs):
        pending_notifications = Notification.objects.filter(is_sent=False)
        type_of_pending_notifications = list(pending_notifications.values_list("type__code", flat=True).distinct())
        handlers = {}  # to hold instance e.g. {'email' : EmailUtil(),'sms': SMSUtil()}
        for notification_type in type_of_pending_notifications:
            handlers[notification_type] = get_notification_type_handler(notification_type)
        for notification in pending_notifications:
            try:
                params = {}
                params["notification"] = notification
                print("Params")
                print(params)
                handlers[notification.type.code].send(**params)
                notification.is_sent = True
            except Exception as e:
                print("Email sending failed cause")
                print(e)
                print("--------------------------")
                notification.is_sent = False
            notification.save()
