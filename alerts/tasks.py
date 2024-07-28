import requests
from celery import shared_task
from django.core.mail import send_mail
from .models import Alert

@shared_task
def check_price_and_send_email():
    alerts = Alert.objects.filter(status='created')
    for alert in alerts:
        response = requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&ids={alert.coin}')
        current_price = response.json()[0]['current_price']
        if current_price >= alert.target_price:
            alert.status = 'triggered'
            alert.save()
            send_mail(
                'Price Alert Triggered',
                f'The price of {alert.coin} has reached your target price of {alert.target_price}.',
                'your_email@gmail.com',
                [alert.user.email],
            )
