from django.shortcuts import render, redirect
from .forms import ContactForm

# Step 4: Contact view (GET shows form, POST validates)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # If valid (e.g., message is 20+ chars), redirect to success page
            return redirect('thank_you')
    else:
        # If it's a GET request, create an empty form
        form = ContactForm()

    return render(request, 'feedback/contact.html', {'form': form})

# Step 5: Thank you view


def thank_you_view(request):
    return render(request, 'feedback/thank_you.html')
