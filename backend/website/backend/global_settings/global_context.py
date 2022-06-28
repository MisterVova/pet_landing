# from global_settings.utils import get_global_settings
from global_settings.models import DemoGlobal


def get_global_settings():
    try:
        kit_of_values = DemoGlobal.get_solo().kit_of_values.get_value()
    except:
        kit_of_values = {"err": "except"}
    return kit_of_values



def global_context(request, page):
    # from garpix_menu.utils import get_menus
    from global_settings.utils_menu import get_menus

    try:
        menus = get_menus(page.get_absolute_url(), None)
    except Exception:
        # print('Exception')
        menus = {}
    finally:
        pass
    # print("global_context_2(request, page)", request, page)

    global_settings = get_global_settings()
    global_settings.update({"menus": menus})
    return global_settings

