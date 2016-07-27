from django.db import models as db
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class Customer(db.Model):
    user = db.OneToOneField(User, on_delete=db.CASCADE)
    locality = db.ForeignKey('Locality')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = db.CharField(validators=[phone_regex], blank=True, max_length=10) # validators should be a list

    def __str__(self):
        return self.user.username


class Locality(db.Model):
    class Meta:
        verbose_name_plural = "localities"

    address = db.CharField(max_length=200)
    city = db.CharField(max_length=50)
    postal_code_regex = RegexValidator(regex=r'^\d{5}$', message="Postal code must consist to 5 digits.")
    postal_code = db.CharField(validators=[postal_code_regex], blank=True, max_length=5)
    country = db.CharField(max_length=30)

    def __str__(self):
        return self.address


class Car(db.Model):
    COLOR = (
        ('RD', 'Red'),
        ('BK', 'Black'),
        ('WT', 'White'),
        ('LG', 'Light Grey'),
        ('DG', 'Dark Grey'),
        ('OT', 'Other')
    )
    CAR_FUEL = (
        ('GZE', 'Gasoline'),
        ('DSL', 'Diesel'),
        ('ELC', 'Electric'),
        ('GPL', 'GPL'),
    )
    number_id = db.CharField(max_length=10)
    color = db.CharField(max_length=20, choices=COLOR)
    price_day = db.DecimalField(max_digits=5, decimal_places=2)
    brand = db.ForeignKey('CarBrand')
    model = db.ForeignKey('CarModel')
    car_fuel = db.CharField(max_length=3, choices=CAR_FUEL)
    car_category = db.ForeignKey('CarCategory')
    locality = db.ForeignKey('Locality')
    picture = db.ImageField(upload_to='img/')

    def __str__(self):
        return self.number_id


class CarCategory(db.Model):
    class Meta:
        verbose_name_plural = 'car categories'

    name = db.CharField(max_length=50, unique=True)
    content = db.TextField(null=False)
    picture = db.ImageField(upload_to='img/', null=False)

    def __str__(self):
        return self.name


class CarBrand(db.Model):
    brand = db.CharField(max_length=20)

    def __str__(self):
        return self.brand


class CarModel(db.Model):
    model = db.CharField(max_length=20)
    brand = db.ForeignKey('CarBrand')

    def __str__(self):
        return self.model


class Reservation(db.Model):
    id_customer = db.ForeignKey('Customer')
    id_car = db.ForeignKey('Car')
    id_from_locality = db.ForeignKey('Locality', related_name='from_locality')
    id_to_locality = db.ForeignKey('Locality', related_name='to_locality')
    from_date = db.DateTimeField(blank=False)
    to_date = db.DateTimeField(blank=False)
    price_reservation = db.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.id_customer