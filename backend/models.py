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