# Milestone 5
# listings/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(booking_id, user_email):
    """
    Sends a booking confirmation email asynchronously.
    """
    subject = 'Booking Confirmation'
    message = f'Thank you for your booking! Your booking ID is {booking_id}.'
    
    # Use the Django email backend defined in settings.py
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )
