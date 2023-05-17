from django.shortcuts import render,get_object_or_404
from product.models import ProductModel,Category
# Create your views here.

def store(request,category_slug=None):
    categories=None
    products=None
    if category_slug!=None:
        categories=get_object_or_404(Category,slug=category_slug)
        products=ProductModel.objects.filter(category=categories,is_available=True)
        count=products.count()
    else:
        products=ProductModel.objects.all().filter(is_available=True)
        count=products.count()
    context={
        "products":products,
        'count':count
    }
    return render(request,'store.html',context)


def product_details(request,category_slug,product_slug):
    try:
        product_detail=ProductModel.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e

    context={
        'product_detail':product_detail
    }
    return render(request,'product_details.html',context)
