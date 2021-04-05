from django.forms import ModelForm, Form
import django.forms as f
from .models import Telefon, Ocena
from django import forms


class TelefonForm(ModelForm):
    class Meta:
        model = Telefon
        fields = ['marka', 'model', 'memorija', 'boja', 'cena']

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['user', 'ocena'] 

class SearchBrandForm(ModelForm):
    class Meta:
        model = Telefon
        fields = ['marka'] 

class SearchModelForm(ModelForm):
    class Meta:
        model = Telefon
        fields = ['marka', 'model'] 

class SearchPriceForm(ModelForm):
    class Meta:
        model = Telefon
        fields = ['cena']                       