from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator


MOCK_PRODUCTS = [
    {'id': 1, 'name': 'Wireless Mouse', 'category': 'electronics', 'price': 25.99, 'rating': 4.5,
        'description': 'Ergonomic wireless mouse.', 'reviews': 'Great battery life!', 'shipping': '2-3 business days'},
    {'id': 2, 'name': 'Mechanical Keyboard', 'category': 'electronics', 'price': 85.00, 'rating': 4.8,
        'description': 'Clicky switches.', 'reviews': 'Very loud and satisfying.', 'shipping': 'Free shipping'},
    {'id': 3, 'name': 'Python Crash Course', 'category': 'books', 'price': 30.00, 'rating': 4.9,
        'description': 'Learn Python fast.', 'reviews': 'Best book for beginners.', 'shipping': 'Next day delivery'},
    {'id': 4, 'name': 'Coffee Mug', 'category': 'home', 'price': 12.50, 'rating': 4.2,
        'description': 'Ceramic dark mug.', 'reviews': 'Looks elegant.', 'shipping': '5-7 business days'},
    {'id': 5, 'name': 'Gaming Monitor', 'category': 'electronics', 'price': 300.00, 'rating': 4.7,
        'description': '144Hz IPS display.', 'reviews': 'Super smooth gameplay.', 'shipping': 'Heavy item shipping applies'},
]


def product_list(request):
    products = MOCK_PRODUCTS

    q = request.GET.get('q', '').strip().lower()
    if q:
        products = [p for p in products if q in p['name'].lower()
                    or q in p['description'].lower()]

    category = request.GET.get('category', '')
    if category:
        products = [p for p in products if p['category'] == category]

    min_price = request.GET.get('min_price', '')
    if min_price:
        try:

            min_price_float = float(min_price)
            products = [p for p in products if p['price'] >= min_price_float]
        except ValueError:
            pass

    valid_sort_fields = ['price', 'rating', 'name']
    sort_by = request.GET.get('sort', 'name')
    if sort_by not in valid_sort_fields:
        sort_by = 'name'

    products = sorted(products, key=lambda x: x[sort_by])

    paginator = Paginator(products, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'page_obj': page_obj, 'q': q, 'category': category,
        'min_price': min_price, 'sort': sort_by
    })


def product_detail(request, id):
    product = None
    for p in MOCK_PRODUCTS:
        if p['id'] == id:
            product = p
            break

    if not product:
        raise Http404("Product not found")

    valid_tabs = ['details', 'reviews', 'shipping']
    tab = request.GET.get('tab', 'details')
    if tab not in valid_tabs:
        tab = 'details'

    return render(request, 'products/product_detail.html', {'product': product, 'tab': tab})
