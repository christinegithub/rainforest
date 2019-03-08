from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(500)])
    price = models.IntegerField()
    url = models.CharField(max_length  = 255)

    def __str__(self):
        return self.name

    def price_in_dollars(self):
        dollars = self.price / 100
        return "${:.2f}".format(dollars)
