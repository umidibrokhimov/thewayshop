from django.db import models

class HomeSlides(models.Model):
    class Meta():
        verbose_name = 'Slide'
        verbose_name_plural = 'Home Slides'
    
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()