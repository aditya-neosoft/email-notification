from django.contrib import admin
from api.models import Notification, NotificationTemplate, NotificationType

admin.site.register(Notification)
admin.site.register(NotificationTemplate)
admin.site.register(NotificationType)
