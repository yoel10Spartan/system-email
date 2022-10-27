import os
from telnetlib import STATUS
from unittest import result
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status

import stripe

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

import qrcode
import qrcode.image.svg
from io import BytesIO

from weasyprint import HTML
# from weasyprint.fonts import FontConfiguration
from xhtml2pdf import pisa

from django.http import HttpResponse
from django.template.loader import render_to_string

def send_email(email_str: str, context: dict):
    try:
        template = get_template('index.html')
        
        content = template.render(context)
        
        email = EmailMultiAlternatives(
            'Mensaje de confirmación de registro a POSADA EMPRESAS ARIES 2022.',
            'Mensaje de confirmación de registro a POSADA EMPRESAS ARIES 2022.',
            settings.EMAIL_HOST_USER,
            [
                email_str,
                'munozzecuayoel@gmail.com',
                'hola@registroparacongresos.com',
                'comunicacion.corporativa@gda.mx'
            ]
        )
        email.attach_alternative(content, 'text/html')
        email.send()
    except:
        raise Response('Error')

@api_view(['POST'])
def send_email_user(request):
    email = request.data['email']

    context = {
        'id': request.data['id'],
        'full_name': request.data['name']
    }

    for i in range(10):
        send_email(email, context)

    return Response({'ok': True})

# context = {
#         'price_pay': user.price_pay,
#         'user': user,
#         'image': 'https://congreso.icu/media/{}.jpg'.format(user.id),
#         'portada': 'https://congreso.icu/media/portada_photo.jpg'
#     }
    
#     send_email(user.email, context)