from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_tickets']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['num_tickets'].widget.attrs.update({'min': 1})

