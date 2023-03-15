from django.shortcuts import render

from events.models import EventsModel


# Create your views here.
def home(request):
    context = {'events': EventsModel.objects.all(),
               }
    return render(request, 'events/home.html', context)
