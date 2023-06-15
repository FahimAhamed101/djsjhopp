from django.shortcuts import render
from .models import Event
# Create your views here.
def event_page(request, pk):
    event = Event.objects.get(id=pk)
    
    

    
        
    return render(request, 'event.html', {'event':event,})