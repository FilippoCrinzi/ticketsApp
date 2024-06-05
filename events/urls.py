# events/urls.py

from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateView, home_view

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventRetrieveUpdateView.as_view(), name='event-detail'),
    path('', home_view, name='home'),
]
