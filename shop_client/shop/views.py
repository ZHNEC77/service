import requests
from django.shortcuts import render
from django.conf import settings

API_URL = 'http://127.0.0.1:8000/api/'  # URL серверной части

def product_list(request):
    response = requests.get(f'{API_URL}products/')
    products = response.json()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    response = requests.get(f'{API_URL}products/{pk}/')
    product = response.json()
    return render(request, 'shop/product_detail.html', {'product': product})

def decrease_quantity(request, pk):
    quantity = request.POST.get('quantity', 0)
    response = requests.post(f'{API_URL}products/{pk}/decrease_quantity/', data={'quantity': quantity})
    if response.status_code == 200:
        return render(request, 'shop/success.html')
    else:
        return render(request, 'shop/error.html', {'error': response.json().get('error')})