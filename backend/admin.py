from django.contrib import admin
from django.contrib.auth.models import User
from backend.models import Customer, Car, CarBrand, Locality, CarModel, Reservation
# Register your models here.


admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(Locality)
admin.site.register(CarModel)
admin.site.register(Reservation)