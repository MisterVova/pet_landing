# from global_settings.utils import get_global_settings
from global_settings.models import DemoGlobal


def get_global_settings():
    try:
        # kit_of_values = "try_1"
        kit_of_values = DemoGlobal.get_solo().kit_of_values.get_value()
        # kit_of_values = "try_2"
    except:
        # kit_of_values = None
        kit_of_values = {"err": "except"}

    return kit_of_values
    # return {
    #     "my": " мои Глобальные настройки ",
    #     "kit_of_values": kit_of_values,
    #     # "logo": LogoSerializer(Logo.get_solo()).data,
    #     # "privacy_policy": PrivacyPolicySerializer(PrivacyPolicy.get_solo()).data,
    # }


def global_context(request, page):
    from garpix_menu.utils import get_menus
    menus = get_menus(page.get_absolute_url())
    return {
        "menus": menus,
        "global_settings": get_global_settings(),
    }


def global_context_2(request, page):
    from garpix_menu.utils import get_menus
    # menus = None
    try:
        menus = get_menus(page.get_absolute_url())
    except Exception:
        print('Exception')
        menus = None
    finally:
        pass
    print("global_context_2(request, page)", request, page)

    global_settings = get_global_settings()
    global_settings.update({"menus": menus})
    return global_settings
    # return {
    #     "menus": menus,
    #     "global_settings": get_global_settings(),
    # }
