from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(HomeSlides)
class HomeSlidesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(TeamMembers)
class TeamMembersTranslationOptions(TranslationOptions):
    fields = ('name', 'profession', 'about')

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(BrandCategories)
class BrandCategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)