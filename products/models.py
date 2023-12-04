from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    flag_type=[
        ('New','New'),
        ('Sale','Sale'),
        ('Feature','Feature'),
    ]
    name=models.CharField(max_length=120,verbose_name=_('name_product'))
    price=models.DecimalField(_('price'),max_digits=6,decimal_places=2)
    flag=models.CharField(_('flag'),max_length=25,choices=flag_type)
    sku=models.IntegerField(_('sku'))
    subtitle=models.TextField(_('subtitle'),max_length=300)
    descriptions=models.TextField(_('descriptions'),max_length=5000)
    image=models.ImageField(_('image'),upload_to='photo_product')
    tags = TaggableManager()
    slug=models.SlugField(_('slug'),null=True,blank=True)
    brand=models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=self.name
        super(Product,self).save(*args,**kwargs)

class Image(models.Model):
    prouct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='image_product',verbose_name=_('product'))
    image=models.ImageField(_('image'),upload_to='photos_prouct/%y-%m-%d')

    def __str__(self):
        return str(self.product)
    
class Brand(models.Model):
    name=models.CharField(max_length=100,verbose_name=_('name'))
    image=models.ImageField(upload_to='photo_brand%y-%m-%d',verbose_name=_('image'))

    def __str__(self):
        return self.name
    
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='review_product',verbose_name=_('product'))
    review=models.TextField(max_length=150,verbose_name=_('review'))
    rate=models.IntegerField(choices=[(i,i) for  i in range(1,6)])
    publish_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.product)





    

