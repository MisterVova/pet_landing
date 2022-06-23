from modeltranslation.translator import TranslationOptions, register
from ..models import CasesPage


@register(CasesPage)
class CasesPageTranslationOptions(TranslationOptions):
    pass
