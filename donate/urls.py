from django.urls import path, include
from .views import donate, charge, success, cancel

urlpatterns = [
    path('donate/', donate, name='donate'),
    path('donate/charge/', charge, name='charge'),
    path('donate/success/', success, name='success'),
    path('donate/cancel/', success, name='cancel')
] 