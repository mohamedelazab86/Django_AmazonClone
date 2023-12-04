from django.contrib import admin
from .models import Product,Brand,Image,Review
from django_summernote.admin import SummernoteModelAdmin

class Productadmin(SummernoteModelAdmin):
    list_display=['name','price','flag']
    list_filter=['brand']
    search_fields=['name']
    summernote_fields = ('subtitle','descriptions')

# Register your models here.
admin.site.register(Product,Productadmin)
admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Review)
