from django.http import HttpResponse
from .tasks import send_welcome_email

def trigger_email(request):
    send_welcome_email.delay("abdullaharshed956@gmail.com")
    return HttpResponse("Email task triggered")
