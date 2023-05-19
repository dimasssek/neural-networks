from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .models import *
from .forms import ExpeditionForm

def index(request):
    planets = Planet.objects.all()
    astronauts = Astronaut.objects.all()
    expeditions = Expedition.objects.all()
    data = {'planets': planets, 'astronauts': astronauts, 'expeditions': expeditions}
    return render(request, "Space/index.html", data)

def create(request):
    if request.method == 'POST':
        form = ExpeditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = ExpeditionForm()
    context = {
        'form': form
    }
    return render(request, "Space/create.html", context)

class ExpeditionChange(UpdateView):
    model = Expedition
    template_name = 'Space/change.html'
    form_class = ExpeditionForm
