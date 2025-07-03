from celery import shared_task
import time

@shared_task
def send_welcome_email(user_email):
    time.sleep(5)
    print("✅ Welcome email sent!")
    return "Done"
