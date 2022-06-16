from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.
admin.site.register(User)
# admin.site.register(TeamMembers)
# admin.site.register(Blog)
# admin.site.register(Products)
# admin.site.register(Categories)
admin.site.register(BrandCategories)

@admin.register(HomeSlides)
class HomeSlidesAdmin(TranslationAdmin):
    pass

# @admin.register(User)
# class HomeSlidesAdmin(TranslationAdmin):
#     pass

@admin.register(TeamMembers)
class HomeSlidesAdmin(TranslationAdmin):
    pass

@admin.register(Blog)
class HomeSlidesAdmin(TranslationAdmin):
    pass

@admin.register(Products)
class HomeSlidesAdmin(TranslationAdmin):
    pass

@admin.register(Categories)
class HomeSlidesAdmin(TranslationAdmin):
    pass
