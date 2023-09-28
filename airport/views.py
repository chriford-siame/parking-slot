import math
import random
import environ
import requests
from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_http_methods

# env = environ.Env()
# environ.Env.read_env()


def process_payment(plan, amount):
    auth_token = 'FLWSECK_TEST-a987ec54fe7b47dfa301709a3a4096d5-X'
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {
        "tx_ref": ''+str(math.floor(1000000 + random.random()*9000000)),
        "amount": amount,
        "currency": "ZMW",
        "redirect_url": "http://localhost:8001/payment/callback",
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
            "title": f"Plan - {plan.title()}",
            "description": "AirportZ payment form",
            "logo": "https://www.moderncremation.ca/wp-content/uploads/PaymentGateway.jpg"
        }
    }
    url = ' https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response = response.json()
    print(response)
    return response['data']['link']


def index(request):
    context = {
        'airports': [
            {

                'index': '01',
                'name': 'Keneth Kauda',
            },
            {
                'index': '02',
                'name': 'Kabwe',
            },
            {
                'index': '03',
                'name': 'CIP',
            },
            {
                'index': '04',
                'name': 'Chipata',
            },
            {
                'index': '05',
                'name': 'Solwezi',
            },
            {
                'index': '06',
                'name': 'Mfuwe',
            },
            {
                'index': '07',
                'name': 'Livingstone',
            },
        ]
    }
    
    return render(request, 'other/index.html', context)


def about(request):
    return render(request, 'other/about.html')


def contact(request):
    return render(request, 'other/contact.html')


def blogs(request):
    return render(request, 'other/blogs.html')


def blog(request):
    return render(request, 'other/blog.html')


def payment_processor(request):
    payment_form_url = str(process_payment())
    return redirect(payment_form_url)


def parking_slot_view(request, airport):
    message = ''
    if request.method == 'POST':
        entry_date = request.POST.get('entry-date')
        entry_time = request.POST.get('entry-time')
        if entry_date == '2023-09-22':
            message = 'The parking slot at the selected entry date has been occupied, enter another one.'
        else:
            return redirect('slot_plans')

    return render(request, 'other/slot-view.html', {'airport': airport})
    # return render(request, 'temp/property-single.html', {'airport': airport, 'message': message})


def parking_slot_plans(request):
    if request.method == 'POST':
        plan = request.POST.get('plan', None)
        if plan:
            amount = request.POST.get('amount', 0)
            if amount == 0 and isinstance(amount, int):
                messages.add_message(
                    request, messages.ERROR, 'An error occurred while, contact support for help.')
                return redirect('index')
            obj = dict(
                plan=plan,
                amount=int(amount),
            )
            # TODO: query the plan dynamically by submitted plan
            return redirect(
                str(process_payment(obj['plan'], obj['amount']))
            )
        else:
            return redirect('index')
    return render(request, 'other/plans.html')


@require_http_methods(['GET', 'POST'])
def payment_response(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    print(status)
    print(tx_ref)
    return render(request, 'payment/payment_callback.html', {
        'payment_status': status,
        'tx_ref': tx_ref,
    })

def payment_fail(request):
    return render(request, 'payment/fail.html')

def payment_success(request):
    return render(request, 'payment/success.html')

def analytics(request):
    return render(request, 'other/analytics.html')


def notifications(request):
    return render(request, 'other/notifications.html')


def guide(request):
    return render(request, 'other/guide.html')
