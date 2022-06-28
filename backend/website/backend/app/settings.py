from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    "show",
    "kit_of_values",
    "landing",
    "applications",
    "global_settings",
    "pages",
    "staff",
    "forms",

]


GARPIX_PAGE_GLOBAL_CONTEXT = "global_settings.global_context.global_context"
# GARPIX_PAGE_GLOBAL_CONTEXT = "app.global_settings.global_settings"


MENU_TYPE_HEADER_MENU_BURGER = 'header_menu_burger'
MENU_TYPE_FOOTER_MENU_BURGER = 'footer_menu_burger'

MENU_TYPES = {
    MENU_TYPE_HEADER_MENU_BURGER: {
        'title': 'Header menu burger',
    },
    MENU_TYPE_FOOTER_MENU_BURGER: {
        'title': 'Footer menu burger',
    },
}

CHOICE_MENU_TYPES += [(k, v['title']) for k, v in MENU_TYPES.items()]
