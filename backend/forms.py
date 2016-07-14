from django.forms import ModelForm
from backend.models import Customer, CarBrand, Car, Locality


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CarBrandForm(ModelForm):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class LocalityForm(ModelForm):
    class Meta:
        model = Locality
        fields = '__all__'