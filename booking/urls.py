from django.urls import path
from . import views

urlpatterns = [
    path('booking/<int:event_id>/', views.booking_view, name='booking'),
    path('success/<int:booking_id>/', views.payment_success, name='payment_success'),]

