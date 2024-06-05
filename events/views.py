from rest_framework import generics, filters
from .models import Event
from .serializers import EventSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date']  # Filtra per data
    search_fields = ['title', 'description']  # Cerca per titolo e descrizione

class EventRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


def home_view(request):
    query = request.GET.get('search')
    if query:
        events = Event.objects.filter(title__icontains=query) | Event.objects.filter(description__icontains=query)
    else:
        events = Event.objects.all()
    return render(request, 'home.html',{'events': events, 'query': query})