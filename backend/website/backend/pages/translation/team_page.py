from modeltranslation.translator import TranslationOptions, register
from ..models import TeamPage


@register(TeamPage)
class TeamPageTranslationOptions(TranslationOptions):
    pass
