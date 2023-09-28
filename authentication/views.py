from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from authentication.models import User
from django.contrib.auth import authenticate, login as login_user, logout

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        alternative_phone_number = request.POST.get('phone_number2')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            return redirect('signup')

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            alternative_phone_number=alternative_phone_number,
        )
        user.save()
        user.is_superuser = True
        user.set_password(password)
        user.save()
        # assign roles here
        user_obj = authenticate(
            username=username, 
            password=password
        )
        if user_obj != None:
            login_user(request, user_obj)
            return HttpResponseRedirect('/')
        else:
            return redirect('signup')
    context = dict()
    return render(request, 'account/register.html', context)

def login(request):
    if request.method == 'POST':
        unique_identifier = request.POST.get('unique-identifier')
        password = request.POST.get('password')
        user_exists = authenticate(username=unique_identifier, password=password)
        if user_exists != None:
            user = user_exists
            login_user(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login/')
    return render(request, 'account/login.html')

def profile(request):
    ctx = {
        "range": [
            {
                "id": 1,
                "image_name": "post-8",
                "status": "Succeeded",
                'airport': 'Chipata',
            },
            {
                "id": 2,
                "image_name": "post-8",
                "status": "Succeeded",
                'airport': 'Solwezi',
                
            },
            {
                "id": 3,
                "image_name": "post-8",
                "status": "Succeeded",
                'airport': 'Mfuwe',
                
            },
            {
                "id": 4,
                "image_name": "post-8",
                "status": "Cancelled",
                'airport': 'Livingstone',
                
            },
        ]
    }
    return render(request, 'account/profile.html', ctx)
