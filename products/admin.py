from django.contrib import admin
from .models import Product,Brand,Image,Review

# Register your models here.
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Review)
