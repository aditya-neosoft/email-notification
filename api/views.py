# -*- coding: utf-8 -*-
"""
Implement API views here.

Implements the API views for notification service.
"""
from django.core.management import call_command

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
from rest_framework.views import Response

from api.models import Notification, NotificationTemplate, NotificationType
from api.serializers import NotificationSerializer, \
    NotificationTemplateSerializer, NotificationModelSerializer
from api.utils.send_email import send_email_template


class NotificationViewSet(ViewSet):
    """This class is for REST apis related to Notification service."""

    def create(self, request):
        """
        To create a new notification.

        :param request:
        :return:
        """

        serializer_class = NotificationSerializer(data=request.data)
        try:
            request.data._mutable = True
        except AttributeError:
            pass
        if serializer_class.is_valid():
            # import ipdb; ipdb.set_trace()
            template_id = NotificationTemplate.objects.get(
                name__icontains=request.data.get("template_name"),
            ).id
            notification_type_id = NotificationType.objects.get(
                code__icontains=request.data.get("notification_type"),
            ).id
            request.data["template"] = template_id
            request.data["type"] = notification_type_id
            serializer_class = NotificationModelSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                send_email_notification(request.data.get("template_name"),request.data.get("receiver"),request.data.get("subject"),**eval(request.data.get('params')))
                call_command("send_notifications")
            else:
                return Response(
                    {
                        'data': request.data,
                        'message': serializer_class.errors,
                        'status': False,
                    }, status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                {
                    'data': serializer_class.data,
                    'message': 'Notification created successfully.',
                    'status': True,
                }, status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    'data': request.data,
                    'message': serializer_class.errors,
                    'status': False,
                }, status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """
        To retrieve all notifications for specific user.

        :param request:
        :return:
        """
        try:
            notifications = Notification.objects.get(id=pk)
            return Response(
                {
                    'data': NotificationModelSerializer(notifications).data,
                    "status": True,
                    "message": "Notification retrieved successfully.",
                },
                status=status.HTTP_200_OK,
            )
        except Notification.DoesNotExist:
            return Response(
                {
                    'message': "Notification doesn't exist.", 'status': False,
                    "data": None,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def destroy(self, request, pk):
        """
        To delete a notification

        :param request:
        :param pk:
        :return:
        """
        try:
            Notification.objects.get(id=pk).delete()
            return Response(
                {
                    'message': 'Notifications deleted successully.',
                    'status': True, "data": None,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except Notification.DoesNotExist:
            return Response(
                {
                    'message': "Notification doesn't exist.",
                    'status': False, "data": None,
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class NotificationTemplateViewSet(ModelViewSet):
    """This class is for REST apis related to Notification Template service."""

    queryset = NotificationTemplate.objects.all()
    serializer_class = NotificationTemplateSerializer
