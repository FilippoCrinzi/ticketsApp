from django.contrib import admin
from .models import Booking

admin.site.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event', 'num_tickets', 'status', 'created_at']