from modeltranslation.translator import TranslationOptions, register
from ..models import CasePage


@register(CasePage)
class CasePageTranslationOptions(TranslationOptions):
    pass
