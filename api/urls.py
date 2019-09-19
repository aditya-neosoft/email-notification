from rest_framework.routers import DefaultRouter
from api.views import NotificationViewSet, NotificationTemplateViewSet

router = DefaultRouter()
router.register('notifications', NotificationViewSet,
                base_name='notifications')
router.register('notification-template', NotificationTemplateViewSet,
                base_name='notification_template')
urlpatterns = router.urls
