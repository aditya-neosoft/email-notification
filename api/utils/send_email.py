from api.models import *
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail

def send_email_template(template_name, receivers, subject,**kwargs):
	try:
		# htmly = get_template('email_template_1.html')
		# import ipdb; ipdb.set_trace()
		template_obj = NotificationTemplate.objects.get(name=template_name)
		html_code = template_obj.content.format(**kwargs)

		# html_content = htmly.render({'first_name':first_name})
		# html_code = 'This Sample Templ {}'.format('Aditya')
		
		msg = EmailMultiAlternatives(subject, '', settings.EMAIL_HOST_USER, [receivers])
		msg.attach_alternative(html_code, "text/html")
		msg.send()
		
		return {'msg': 'mail sent successfully!', 'type': 'success'}
	except Exception as e:
		return {'msg': str(e), 'type': 'error'}