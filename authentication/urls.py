from django.urls import path, include
from .views import login, register, logout, profile

app_name = 'authentication'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='user-profile'),
]