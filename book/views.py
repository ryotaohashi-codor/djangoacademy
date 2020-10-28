from django.shortcuts import render
from django.http import HttpResponse

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Create your views here.

def sendmail(request):
    message = Mail(
        from_email='support@django-academy.net',
        to_emails='ryotaohashi.codor@gmail.com',
        subject = 'title',
        html_content= 'contentcontent'
    )
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    return HttpResponse('email')