from dataclasses import fields
from django.forms import ModelForm
from . import models

class GameForm(ModelForm):
    class Meta:
        model=models.Game
        fields="__all__"