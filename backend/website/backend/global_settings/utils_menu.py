from django.conf import settings
from django.forms.models import model_to_dict
from garpix_menu.models import MenuItem


def check_is_home(url):
    urls = ['', '/']
    for item in settings.LANGUAGES:
        urls.append(f'/{item[0]}')
    return url in urls


def get_menus(current_path, parent=None):
    current_path_without_slash = current_path
    if current_path_without_slash[-1] == '/':
        current_path_without_slash = current_path_without_slash[0:-1]

    menus = {}
    for menu_type_arr in settings.CHOICE_MENU_TYPES:
        menu = MenuItem.objects.filter(is_active=True, menu_type=menu_type_arr[0], parent=parent)
        menus[menu_type_arr[0]] = []
        for menu_item in menu.order_by('sort', 'title'):
            link = menu_item.get_link()
            if link in (current_path, current_path_without_slash):
                menu_item.is_current = True
                menu_item.is_current_full = True
            elif current_path.startswith(link):
                if not check_is_home(link):
                    menu_item.is_current = True
            elif menu_item.url and menu_item.url.endswith(current_path):
                if not check_is_home(link):
                    menu_item.is_current = True
            menus[menu_type_arr[0]].append(model_to_dict(menu_item))
            menus[menu_type_arr[0]][-1]['get_link'] = link
            menus[menu_type_arr[0]][-1]['is_current'] = menu_item.is_current
            menus[menu_type_arr[0]][-1]['is_current_full'] = menu_item.is_current_full
            try:
                menus[menu_type_arr[0]][-1]['icon'] = menu_item.icon.url
            except:
                menus[menu_type_arr[0]][-1]['icon'] = None
            menus[menu_type_arr[0]][-1].pop('page', None)
            menus[menu_type_arr[0]][-1].pop('title_for_admin', None)

            submenu_items = get_submenu(current_path, parent=menu_item)
            # print("submenu_items", submenu_items)
            if len(submenu_items):
                menus[menu_type_arr[0]][-1]["submenu"] = submenu_items

    return menus


def get_submenu(current_path, parent):
    if not type(parent) == MenuItem:
        return []

    current_path_without_slash = current_path
    if current_path_without_slash[-1] == '/':
        current_path_without_slash = current_path_without_slash[0:-1]

    menus = MenuItem.objects.filter(is_active=True, parent=parent)
    submenu = []
    for menu_item in menus.order_by('sort', 'title'):
        link = menu_item.get_link()
        if link in (current_path, current_path_without_slash):
            menu_item.is_current = True
            menu_item.is_current_full = True
        elif current_path.startswith(link):
            if not check_is_home(link):
                menu_item.is_current = True
        elif menu_item.url and menu_item.url.endswith(current_path):
            if not check_is_home(link):
                menu_item.is_current = True
        submenu.append(model_to_dict(menu_item))
        submenu[-1]['get_link'] = link
        submenu[-1]['is_current'] = menu_item.is_current
        submenu[-1]['is_current_full'] = menu_item.is_current_full
        try:
            submenu[-1]['icon'] = menu_item.icon.url
        except:
            submenu[-1]['icon'] = None
        submenu[-1].pop('page', None)
        submenu[-1].pop('title_for_admin', None)

        submenu_items = get_submenu(current_path, parent=menu_item)
        if len(submenu_items):
            submenu[-1]["submenu"] = submenu_items
    return submenu
