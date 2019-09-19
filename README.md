# email-notification
Add EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_BACKEND to settings file.

While calling url "/notification/api/v1/notifications/" We have to pass *notification_type,template_name,receiver,params, subject*

In *params* we have to pass dictionary (which will include all keys that are mentioned in template)

