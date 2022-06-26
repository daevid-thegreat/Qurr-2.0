from django.urls import path
from shortener.views import index, shortner, redirect_url

urlpatterns = [
    path('', index, name='Home'),
    path('shortener', shortner, name='Shortener'),
    path('redirect/<str:url>', redirect_url, name='redirect'),
]
