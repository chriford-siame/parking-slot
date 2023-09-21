from django.shortcuts import render, redirect, HttpResponse
import math
import requests
import random
import environ
from rest_framework.response import Response

# env = environ.Env()
# environ.Env.read_env()

def process_payment():
    auth_token = 'FLWSECK_TEST-46ebaa390394ca4757db93674275792a-X'
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {
        "tx_ref": ''+str(math.floor(1000000 + random.random()*9000000)),
        "amount": 2100,
        "currency": "ZMW",
        "redirect_url": "http://localhost:8001/payment/success",
        "payment_options": "card, ZBMobile",
        "meta": {
            "consumer_id": 23,
            "consumer_mac": "92a3-912ba-1192a"
        },
        "customer": {
            "email": 'chrifordsiame@booknowzambia.com',
            "phonenumber": '0762412680',
            "name": 'Chriford Siame'
        },
        "customizations": {
            "title": "Parking Slot",
            "description": "",
            "logo": "https://www.moderncremation.ca/wp-content/uploads/PaymentGateway.jpg"
        }
    }
    url = ' https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response = response.json()
    link = response['data']['link']
    return link


def index(request):
    return render(request, 'other/index.html')

def about(request):
    return render(request, 'other/about.html')

def contact(request):
    return render(request, 'other/contact.html')

def blogs(request):
    return render(request, 'other/airport-grid.html')

def blog(request):
    return render(request, 'other/blog-single.html')

def payment_processor(request):
    return redirect(str(process_payment()))

def payment_fail(request):
    return render(request, 'payment/success.html')

def parking_slot_validity(request):
    
    return render(request, 'other/plans.html')

def parking_slot_plans(request):
    return render(request, 'other/plans.html')

def payment_success(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    return render(request, 'payment/fail.html')
