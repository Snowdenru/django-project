from weather.models import City
from django.forms import ModelForm

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ('name', )
        labels = {"name": "Введите город"}



