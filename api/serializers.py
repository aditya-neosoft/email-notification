from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from api.models import NotificationTemplate, Notification


class NotificationSerializer(serializers.Serializer):
    """
    Serializer class for Notification REST APIs
    """
    notification_type = serializers.CharField(label=_("notification_type"),
                                              required=True)
    template_name = serializers.CharField(label=_("template_name"),
                                          required=True)


class NotificationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class NotificationTemplateSerializer(serializers.ModelSerializer):
    """
    Model Serializer class for listing all notification templates
    """

    class Meta:
        model = NotificationTemplate
        fields = "__all__"
