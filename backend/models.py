from unicodedata import name
from django.db import models

class HomeSlides(models.Model):
    class Meta():
        verbose_name = 'Slide'
        verbose_name_plural = 'Home Slides'
    
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()

class HomeCategories(models.Model):
    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Home Categories'
    
    image = models.ImageField()
    title = models.CharField(max_length=5)

class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog posts'
    
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()

class TeamMembers(models.Model):
    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
    
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    about = models.TextField()
    image = models.ImageField()
    fb_account = models.URLField(max_length=20, null=True, blank=True)
    tr_account = models.URLField(max_length=20, null=True, blank=True)
    gl_account = models.URLField(max_length=20, null=True, blank=True)
    yt_account = models.URLField(max_length=20, null=True, blank=True)

# Products model
class Products(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()

# Categories model
class Categories(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=20)

# Products categories model
class ProductCategories(models.Model):
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
    
    name = models.CharField(max_length=20)

# Brand categories
class BrandCategories(models.Model):
    class Meta:
        verbose_name = 'Brand Category'
        verbose_name_plural = 'Brand Categories'
    
    name = models.CharField(max_length=20)