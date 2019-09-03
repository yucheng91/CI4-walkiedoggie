from django.shortcuts import render, reverse, HttpResponse
from django.conf import settings
import stripe


def donate(request):
    return render(request, 'donate.html')
    
def charge(request):
    amount = int( request.GET['amount']) * 100
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(payment_method_types=['card'],
        line_items=[
            {
                'name': 'Donation',
                'description':'A simple donation',
                'amount':amount ,
                'currency':'sgd',
                'quantity':1
            }
        ],
        success_url= request.build_absolute_uri(reverse('success')),
        cancel_url= request.build_absolute_uri(reverse('cancel')),
    )
    return render(request, 'charge.html', {
        'CHECKOUT_SESSION_ID': session.id,
        'publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })
    
   
    
def success(request):
    return render(request,'success.html')
    
def cancel(request):
    return render(request,'cancel.html')
    
    
    