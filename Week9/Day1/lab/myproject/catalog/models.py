from django.db import models

# Define the Product model inheriting from Django's base Model


class Product(models.Model):

    # Step: Add Category.TextChoices to provide standardized dropdown options
    class Category(models.TextChoices):
        ELECTRONICS = 'EL', 'Electronics'
        CLOTHING = 'CL', 'Clothing'
        FOOD = 'FD', 'Food'

    # Step: Add unique sku and required name fields
    # Unique identifier for the product
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)  # Required product name

    # Step: Add optional description using blank=True (allows empty input in Django forms)
    description = models.TextField(blank=True)

    # Link the category field to the TextChoices defined above
    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.ELECTRONICS
    )

    # Step: Add DecimalField for exact currency precision and PositiveIntegerField for non-negative stock
    # Prevents math rounding errors
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Friendly validation for positive numbers
    stock = models.PositiveIntegerField(default=0)

    # Step: Add status and timestamp fields
    # Soft delete/availability flag
    is_active = models.BooleanField(default=True)
    # Automatically set when created
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically set when saved/updated
    updated_at = models.DateTimeField(auto_now=True)

    # Add metadata, indexes, and constraints (Model Strengthening)
    class Meta:
        # Step: Set default ordering by category then name
        ordering = ['category', 'name']

        # Step: Add clear singular and plural verbose names for the Django Admin interface
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

        # Step: Add a composite index on category and is_active to speed up database lookups
        indexes = [
            models.Index(fields=['category', 'is_active']),
        ]

        # Step: Add named constraints requiring price and stock to be non-negative strictly at the database level
        constraints = [
            models.CheckConstraint(check=models.Q(
                price__gte=0), name='price_non_negative'),
            models.CheckConstraint(check=models.Q(
                stock__gte=0), name='stock_non_negative'),
        ]

    # Step: Add __str__() to return the product name when the object is printed
    def __str__(self):
        return self.name

    # Step: Add custom method is_available() using is_active and stock (Business Logic)
    def is_available(self):
        return self.is_active and self.stock > 0

    # Step: Add custom method inventory_value() using price and stock (Business Logic)
    def inventory_value(self):
        return self.price * self.stock


# ==========================================
# Exit Ticket Answer
# ==========================================
# Q: Explain why non-negative stock deserves both friendly validation and a database constraint.
#
# A: Friendly validation (like PositiveIntegerField) provides clear, immediate error messages
# to the user in forms, improving User Experience (UX). A database constraint (CheckConstraint)
# provides strict data integrity at the database level, ensuring negative stock can never
# be saved even if form validation is bypassed (e.g., via raw SQL or bulk updates).
