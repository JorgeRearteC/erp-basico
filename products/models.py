from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    cuit = models.CharField(max_length=11, unique=True)  # CUIT único de 11 caracteres
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_ORIGIN_CHOICES = [
        ('OWN', 'Propio'),
        ('SUP', 'Proveedor'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    origin = models.CharField(
        max_length=3,
        choices=PRODUCT_ORIGIN_CHOICES,
        default='OWN'
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    
    supplier_products = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="related_products")
    

    def __str__(self):
        return f"{self.name} ({self.get_origin_display()})"