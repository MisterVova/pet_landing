from modeltranslation.translator import TranslationOptions, register
from ..models import LandingPage


@register(LandingPage)
class LandingPageTranslationOptions(TranslationOptions):
    pass
