# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# python3 backend/manage.py startpage --app=home --page=home --base=page


class MrApp:
    blog = "blog"
    comment = "comment"

    global_settings = "global_settings"
    home = "home"
    hotels = "hotels"
    blocks = "blocks"

    templates = "templates"
    show = "show"


class MrPage:
    post = "post"
    posts_list = "posts_list"
    comment = "comment"
    home = "home"
    hotels = "hotels"




class PageType:
    page="page"
    list="list"
    search="search"





def getCommands():
    commands = [
        # f"python3 backend/manage.py startpage --app={MrApp.blog} --page={MrPage.post} --base={PageType.page}",
        # f"python3 backend/manage.py startpage --app={MrApp.blog} --page={MrPage.posts_list} --base={PageType.list}",
        # f"python3 backend/manage.py startpage --app={MrApp.comment} --page={MrPage.comment} --base={PageType.page}",
        "",
        "cd backend",
        f"python3 manage.py startapp {MrApp.global_settings}",
        f"python3 manage.py startapp {MrApp.show}",
        "cd ..",
        "",
        f"python3 backend/manage.py startpage --app={MrApp.home} --page={MrPage.home} --base={PageType.page}",
        f"python3 backend/manage.py startpage --app={MrApp.hotels} --page={MrPage.hotels} --base={PageType.page}",
    ]
    return commands


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    commands= getCommands();
    for c in commands:
        print(c)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/