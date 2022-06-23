from modeltranslation.translator import TranslationOptions, register
from ..models import ZeroPage


@register(ZeroPage)
class ZeroPageTranslationOptions(TranslationOptions):
    pass
