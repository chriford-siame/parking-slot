from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import generic
from airport.views import (
    blogs, 
    blog, 
    index, 
    about, 
    contact, 
    payment_fail, 
    payment_success,
    payment_processor,
    parking_slot_view,
    parking_slot_plans,
    payment_response,
    analytics,
    notifications,
    guide,
    # reservations,
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blogs/', blogs, name='blogs'),
    path('blog/', blog, name='blog'),
    path('slot/<str:airport>/view/', parking_slot_view, name='slot_view'),
    path('slot/plans/', parking_slot_plans, name='slot_plans'),
    path('analytics/', analytics, name='analytics'),
    path('notifications/', notifications, name='notifications'),
    path('guide/', guide, name='guide'),
    
    path('payment/callback/', payment_response, name='payment_response'),
    path('payment/success/', payment_success, name='success'),
    path('payment/fail/', payment_fail, name='fail'),
    path('payment/', payment_processor, name='payment_processor'),

    path('admin/', admin.site.urls),
    path('', include('authentication.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
