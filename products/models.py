from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Este es el campo ID
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
