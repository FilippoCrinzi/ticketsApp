# booking/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from events.models import Event
from .models import Booking
from .forms import BookingForm

@login_required
def booking_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    total_price = 0
    if request.method == 'POST':
        form = BookingForm(request.POST, initial={'event_id': event_id})
        if form.is_valid():
            num_tickets = form.cleaned_data['num_tickets']
            total_price = num_tickets * event.ticket_price
            # La logica del pagamento sarà aggiunta qui in futuro
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            booking.status = 'pending'
            booking.save()
            event.available_seats -= num_tickets
            event.save()
            messages.success(request, 'Prenotazione effettuata con successo.')
            return redirect('home')
    else:
        form = BookingForm(initial={'event_id': event_id})
    return render(request, 'booking/booking.html', {'form': form, 'event': event, 'total_price': total_price})
