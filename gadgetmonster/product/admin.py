from django.contrib import admin
from .models import ProductModel
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','stock','price','is_available','modified_date')
    prepopulated_fields={'slug':('name',)}

admin.site.register(ProductModel,ProductAdmin)