from django.contrib import admin
from django.contrib.auth.models import User
from backend.models import Customer, Car, CarBrand, Locality, CarModel, Reservation, CarCategory
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ['number_id', 'color', 'price_day', 'brand', 'model', 'car_fuel', 'car_category', 'locality',
                    'picture']


class LocalityAdmin(admin.ModelAdmin):
    model = Locality
    list_display = ['address', 'city', 'postal_code', 'country']


class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ['id_customer', 'id_car', 'id_from_locality', 'id_to_locality',
                    'from_date', 'to_date', 'price_reservation']


class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['user', 'locality', 'phone_number']


class CarCategoryAdmin(admin.ModelAdmin):
    model = CarCategory
    list_display = ['name', 'content', 'picture']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarBrand)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(CarModel)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(CarCategory, CarCategoryAdmin)