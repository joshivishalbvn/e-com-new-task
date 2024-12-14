from django.core.mail import send_mail
from django.conf import settings
from app_modules.orders.models import Order



def send_order_confirmation_email(order_id):
    order_obj = Order.objects.filter(id=order_id).first()
    subject = "Order Created Sucessfully"
    print('\033[91m'+'subject: ' + '\033[92m', subject)
    message = f"Hello {order_obj.customer.get_full_name()}  your order is created sucessfully , your oder id : {order_id}"
    print('\033[91m'+'message: ' + '\033[92m', message)
    try:
        send_mail(subject,message,from_email=settings.EMAIL_HOST_USER,recipient_list=[order_obj.customer.email])
    except Exception as e:
        print('\033[91m'+'Exception Occured: ' + '\033[92m', e)
