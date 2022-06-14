from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(HomeSlides)
class HomeSlidesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')