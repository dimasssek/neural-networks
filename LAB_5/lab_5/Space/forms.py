from .models import *
from django.forms import ModelForm, TextInput, DateInput, Select


class ExpeditionForm(ModelForm):
    class Meta:
        planets = Planet.objects.all()
        astronauts = Astronaut.objects.all()
        model = Expedition
        fields = ['expedition_time', 'report', 'planetId', 'astronautId']
        widgets = {
            'expedition_time': TextInput(attrs={
                'class': 'form-control'
            }),
            'report': TextInput(attrs={
                'class': 'form-control'
            }),
            'planetId': Select(choices=planets, attrs={
                'class': 'form-select',
            }),
            'astronautId': Select(choices=astronauts, attrs={
                'class': 'form-select'
            })
        }
