from django.shortcuts import render
from product.models import ProductModel


def home(request):
    products=ProductModel.objects.all().filter(is_available=True)
    context={
        "products":products,
    }
    return render(request,'home.html',context)