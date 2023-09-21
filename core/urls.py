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
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blogs/', blogs, name='blogs'),
    path('blog/', blog, name='blog'),

    path('payment/success/', payment_success, name='success'),
    path('payment/fail/', payment_fail, name='fail'),
    path('payment/', payment_processor, name='payment_processor'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
