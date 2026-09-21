# Guided Lab: Product Model & Strengthening

## Overview
This repository contains the implementation of a Guided Lab focused on building and strengthening a "Product Model" in Django. The primary objective is to translate a single Product entity into Django fields, applying appropriate field types, custom behaviors, metadata, database indexes, and strict database-level constraints to ensure data integrity.

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
7. **Model Methods (Behavior):** 
   - Added the `__str__()` dunder method to return the product's name for better readability.
   - Added `is_available()` to dynamically check if a product is active and in stock.
   - Added `inventory_value()` to calculate the total value of the current stock.
8. **Model Metadata (`class Meta`):**
   - **Ordering:** Configured default ordering by `category` then `name`.
   - **Verbose Names:** Defined clear singular and plural verbose names for the Django Admin interface.
9. **Database Indexing:**
   - Added a composite index on `category` and `is_active` fields to optimize and speed up database query lookups.
10. **Database Constraints:**
    - Added named `CheckConstraint`s (`price_non_negative` and `stock_non_negative`) to strictly ensure price and stock cannot drop below zero at the database level.
11. **Validation:** Executed `python manage.py check` to ensure the model architecture is structurally sound and free of errors.

## Key Concepts Demonstrated (Exit Tickets)
- **Financial Precision:** Used `DecimalField` for the price because financial calculations require strict mathematical accuracy that standard floats cannot guarantee.
- **Form Validation:** Applied `blank=True` to the description field, allowing it to be bypassed during form validation, effectively making the input optional for users.
- **Validation vs. Database Constraints:** Applied `PositiveIntegerField` for friendly, immediate form validation (better UX), and added a `CheckConstraint` for bulletproof data integrity at the database level, ensuring negative stock can never be saved even if application-level validation is bypassed (e.g., via raw SQL or bulk updates).