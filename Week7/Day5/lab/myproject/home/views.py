from django.shortcuts import render, redirect


def home(request):
    user_theme = request.COOKIES.get('theme', 'light')

    # Step 5: Read cart from request.session with [] as default
    cart = request.session.get('cart', [])

    return render(request, 'feedback/home.html', {
        'theme': user_theme,
        'cart': cart,
        'cart_count': len(cart)
    })


def set_theme(request, chosen_theme):
    if chosen_theme not in ['light', 'dark']:
        chosen_theme = 'light'
    response = redirect('home')
    thirty_days = 30 * 24 * 60 * 60
    response.set_cookie('theme', chosen_theme, max_age=thirty_days)
    return response

# Step 6: Add one product ID and save the updated cart


def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('home')

# Step 7: Add clear_cart using session.pop()


def clear_cart(request):
    # Using pop() removes the 'cart' key entirely; we provide [] as a fallback to prevent KeyError
    request.session.pop('cart', [])
    return redirect('home')
