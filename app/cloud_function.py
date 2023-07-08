from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .enc_dec import *
from django.http import JsonResponse
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from datetime import date, timedelta



def send_email(subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "anwarsadik.disk1@gmail.com"
    sender_password = "ogxemcnlxvvbflhx"
    receiver_email = "anwar.se6285@gmail.com"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()


def Notify_Email(request):
    today = datetime.now().date()
    doc = Main_Document_Details.objects.all()
    email_sent = False
    for d in doc:
        if d.document_expiry is not None:
            expiry_date = d.document_expiry
            days_to_expiry = (expiry_date - today).days

            if days_to_expiry == 1:
                print('This document expires in 1 day.')
                subject = "Document Expiry Reminder"
                body = f"Company name: {d.company}\nDocument Name: {d.document_name}\nExpires in 1 day on {expiry_date}."
                send_email(subject, body)
                email_sent = True
    s_doc = Staff_Docs.objects.all()
    for s in s_doc:
        if s.s_documetexp is not None:
            expiry_date = s.s_documetexp
            days_to_expiry = (expiry_date - today).days
            if days_to_expiry == 1:
                subject = "Document Expiry Reminder"
                body = f"Company name : {s.staff.company}\nStaff Name :{s.staff.fullname} \nDocument Name :  {s.s_documetname} \nExpire in 30 days on {expiry_date}."
                send_email(subject, body)
                email_sent = True
    if not email_sent:
        print('No documents expire in 1 day.')
        subject = "Document Expiry Reminder"
        body = f"No Expiry in 30th day"
        send_email(subject, body)

    return HttpResponse()















