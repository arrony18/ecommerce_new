from django.db import models
from categoryApp.models import Category
from django.urls import reverse
# Create your models here.


class ProductModel(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    desc=models.TextField()
    stock=models.PositiveIntegerField()
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photos/Product')
    is_available=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('product_by_slug', args=[self.category.slug,self.slug])
    def __str__(self):
        return self.name