from django.db import models


class Product(models.Model):

    class Category(models.TextChoices):
        ELECTRONICS = 'EL', 'Electronics'
        CLOTHING = 'CL', 'Clothing'
        FOOD = 'FD', 'Food'

    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.ELECTRONICS)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# (Exit ticket):

# DecimalField for price: Prevents rounding errors and ensures exact precision for currency.

# blank=True for description: Makes the field optional in forms, allowing it to be left empty.
