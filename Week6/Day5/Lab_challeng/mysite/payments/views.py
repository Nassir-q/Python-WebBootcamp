from django.shortcuts import render

# Create your views here.


def checkout_view(request):
    return render(request, 'checkout.html')


def receipt_view(request, receipt_id):
    return render(request, 'receipt.html', {'receipt_id': receipt_id})
