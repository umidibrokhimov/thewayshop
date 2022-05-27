from django.db import models

class HomeSlides(models.Model):
    class Meta():
        verbose_name = 'Slide'
        verbose_name_plural = 'Home Slides'
    
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class HomeCategories(models.Model):
    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Home Categories'
    
    image = models.ImageField()
    title = models.CharField(max_length=5)

    def __str__(self):
        return self.title

class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog posts'
    
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self): 
        return self.title

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

    def __str__(self):
        return self.name

# Products model
class Products(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()
    is_sale = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    type_clothe = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True, blank=True)
    brand_clothe = models.ForeignKey('BrandCategories', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

# Categories model
class Categories(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Brand categories
class BrandCategories(models.Model):
    class Meta:
        verbose_name = 'Brand Category'
        verbose_name_plural = 'Brand Categories'
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name