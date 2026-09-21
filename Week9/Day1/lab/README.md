# Guided lab

## Overview
This repository contains the implementation of a Guided Lab focused on building a "Product Model" in Django. The primary objective is to translate a single Product entity into Django fields, applying appropriate field types and constraints.

## Implementation Steps

1. **App Initialization:** Created a new Django app named `catalog` and registered it within the project's `INSTALLED_APPS`.
2. **Model Definition:** Defined the `Product` model inside `catalog/models.py`.
3. **Structured Choices:** Implemented a `Category.TextChoices` nested class to provide standardized category options (Electronics, Clothing, Food).
4. **Text Fields:**
   - `sku`: Defined as a `CharField` with `unique=True` for product identification.
   - `name`: Defined as a required `CharField`.
   - `description`: Defined as a `TextField` with `blank=True` making it optional.
5. **Numeric Fields:**
   - `price`: Defined using `DecimalField` (instead of FloatField) to maintain exact precision for currency and prevent rounding errors.
   - `stock`: Defined using `PositiveIntegerField` to enforce a non-negative inventory count.
6. **Status & Timestamp Fields:**
   - `is_active`: A `BooleanField` defaulting to `True`.
   - `created_at` & `updated_at`: `DateTimeField`s configured to auto-populate upon creation and modification.
7. **Model Methods:** Added the `__str__()` dunder method to return the product's name for better readability in the admin panel and shell.
8. **Validation:** Executed `python manage.py check` to ensure the model architecture is structurally sound and free of errors.

## Key Concepts Demonstrated (Exit Ticket)
- **Financial Precision:** Used `DecimalField` for the price because financial calculations require strict mathematical accuracy that standard floats cannot guarantee.
- **Form Validation:** Applied `blank=True` to the description field, allowing it to be bypassed during form validation, effectively making the input optional for users.