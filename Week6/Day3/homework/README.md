# Django URL Collision Analysis

This repository demonstrates how Django resolves URL paths and how to prevent routing conflicts (collisions) between static strings and dynamic path converters.

## 1. What happens when accessing a product with ID "create"?
When navigating to the URL `/products/create/`, Django evaluates the `urlpatterns` list sequentially from top to bottom. It will encounter `path("products/create/", create_view)` first. Since this is an exact match, Django instantly routes the HTTP request to the `create_view` function. 

The `details_view` will **never** be triggered for the ID "create" because the first matching rule intercepts it.

## 2. How do I view a product where id = "create"?
To view a product with the exact ID "create", the URL architecture must be modified to differentiate between the static action (`create`) and the dynamic variable (`<str:id>`).

**Effective Solutions:**
* **Method A (Add a unique identifier prefix):** Change the details path to `path("products/item/<str:id>/", details_view)`
* **Method B (Change the static action path):** Change the creation path to `path("products/add/new/", create_view)`
* **Method C (Change the data type):** If IDs are only numerical, use `path("products/<int:id>/", details_view)` instead of `<str:id>`.

### Practical Implementation (Method A)

**`urls.py`**
```python
from django.urls import path
from . import views

urlpatterns = [
    # The static route works normally
    path("products/create/", views.create_view, name="create_product"),
    
    # The dynamic route is prefixed with 'id/' to eliminate collision
    path("products/id/<str:id>/", views.details_view, name="product_details"),
]
