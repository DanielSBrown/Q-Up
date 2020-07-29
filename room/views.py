from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Room
from .forms import RoomForm
from .helpers import id_generator

class IndexView(generic.ListView):
  template_name = 'rooms/index.html'
  context_object_name = 'current_room_list'

  def get_queryset(self):
    """Return the last five created rooms."""
    return Room.objects.order_by("-created_date")[:5]

class DetailView(generic.DetailView):
  model = Room
  template_name = "rooms/detail.html"

def create_room(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoomForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            room_name = form.cleaned_data.get('room_name')
            code = id_generator()

            room = Room(code=code, group_name=room_name, created_date=datetime.now())

            room.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/rooms/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RoomForm()

    return render(request, 'rooms/new.html', {'form': form})
