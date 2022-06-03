from django.shortcuts import render
from .models import Category, Drink
# Create your views here.


def product_view(request):
    all_category = Drink.objects.all()
    return render(request, 'menu.html', {'category':all_category})