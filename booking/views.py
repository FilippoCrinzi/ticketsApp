from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from events.models import Event
from .models import Booking
from .forms import BookingForm
import stripe
from django.urls import reverse
from django.http import HttpResponseRedirect

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def booking_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            num_tickets = form.cleaned_data['num_tickets']
            total_price = num_tickets * event.price
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            booking.status = 'pending'
            booking.save()

            # Create a Stripe PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(total_price * 100),  # amount in cents
                currency='eur',
                metadata={'integration_check': 'accept_a_payment'}
            )

            # Save booking as pending

            return render(request, 'booking/payment.html', {
                'client_secret': intent.client_secret,
                'stripe_publishable_key': settings.STRIPE_PUBLIC_KEY,
                'booking_id': booking.id,
                'total_price': total_price,
            })
    else:
        form = BookingForm(initial={'event_id': event_id})
    return render(request, 'booking/booking.html', {'form': form, 'event': event})


@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'confirmed'
    booking.save()

    # Decrease the number of available seats
    booking.event.available_seats -= booking.num_tickets
    booking.event.save()

    messages.success(request, 'Payment successful and booking confirmed!')
    return render(request, 'booking/success.html')
