from django import template

from show.models import Template

register = template.Library()


@register.simple_tag(name="my_tag_test")
def template_test(p1=None, p2=None, p3=None):
    print(type(p1), p1)
    print(type(p2), p2)
    print(type(p3), p3)
    return f"""<h5>::blocks_test::</h5><br>
            p1={type(p1)} | {p1}            <br>
            p2={type(p2)} | {p2}            <br>
            p3={type(p3)} | {p3}            <br>
           """


# template
# @register.simple_tag(name="render_template_to_html")
# def template_render_to_html(blocks, context):
#     ret = ""
#     for block in blocks:
#         ret += f"\n {block.render_to_html(context)}"
#         # try:
#         #     ret += f" {block.render_to_html(context)}"
#         # except Exception:
#         #     pass
#
#     return ret
#
#     # return f"render::{block.render_to_html(context)}::render"

@register.simple_tag(name="render_template")
def render_template_to_html(my_template: Template, kit_of_templates=None, kit_of_values=None):
    # context = {
    #     "object": obj,
    #     "other": other,
    # }
    return my_template.render_template(kit_of_templates=kit_of_templates, kit_of_values=kit_of_values)
    # return f"render::{template.render_to_html(obj,other)}::render"


#
# @register.simple_tag(name="all_context_render_to_html")
# def all_context_render_to_html(templates, context):
#     ret = ""
#     for template in templates:
#         ret += f"\n {template.render_to_html(context)}"
#         # try:
#         #     ret += f" {template.render_to_html(context)}"
#         # except Exception:
#         #     pass
#
#     return ret

@register.simple_tag(name="render_template_by_kit")
def render_template_by_kit_to_html(kit_of_templates: dict = None, kit_of_values: dict = None):
    # print("kit_of_templates", kit_of_templates)
    # print("kit_of_values", kit_of_values)
    if type(kit_of_templates) != dict:
        return f"<h1>Template.DoesNotExist</h1>"

    if kit_of_templates.get("MIX"):
        slug = kit_of_templates.get("dct").get("slug")
    else:
        slug = kit_of_templates.get("slug")

    try:
        my_template = Template.objects.get(slug=slug)
    except Template.DoesNotExist:
        return f"<h1>Template.DoesNotExist</h1><br>slug={slug}<br>kit_of_templates={kit_of_templates}<br>kit_of_values={kit_of_values} "

    return my_template.render_template(kit_of_templates, kit_of_values)


@register.simple_tag(name="render_template_by_slug_test")
def render_template_by_slug_to_html_test(slug, kit_of_templates=None, kit_of_values=None):
    print("slug", slug)
    print("kit_of_templates", kit_of_templates)
    print("kit_of_values", kit_of_values)

    # return f"""
    # <br>slug={slug}
    # <br>kit_of_templates={kit_of_templates}
    # <br>kit_of_values={kit_of_values}
    # <br>
    # """
    # # context = {
    # #     "object": obj,
    # #     "other": other,
    # # }
    from show.models.template import Template
    try:
        my_template = Template.objects.get(slug=slug)
    except Template.DoesNotExist:
        return f"""
                <br>vvvvvvvvvvvvvvvvvvvvvvvvvvvv
                <h1>Template.DoesNotExist</h1>
                <br>slug={slug}
                <br>kit_of_templates={kit_of_templates}
                <br>kit_of_values={kit_of_values} 
                <br>^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """

    return my_template.render_to_html()


@register.simple_tag(name="render_template_context")
def render_template_context_to_html(my_template: Template, kit_of_templates=None, kit_of_values=None, init_object=None, global_context=None):
    context = {
        "kit_of_templates": kit_of_templates,
        "kit_of_values": kit_of_values,
        "object": init_object,
        "global": global_context,
    }

    # return my_template.page_render(kit_of_templates=kit_of_templates, kit_of_values=kit_of_values, init_object=None, global_context=None)
    return my_template.render_template_context(context=context)


@register.simple_tag(name="render_template_context_by_kit")
def render_template_context_by_kit_to_html(kit_of_templates: dict = None, kit_of_values: dict = None, init_object=None, global_context=None):
    if type(kit_of_templates) != dict:
        return f"<h1>Template.DoesNotExist</h1>"

    if kit_of_templates.get("MIX"):
        slug = kit_of_templates.get("dct").get("slug")
    else:
        slug = kit_of_templates.get("slug")

    try:
        my_template = Template.objects.get(slug=slug)
    except Template.DoesNotExist:
        return f"""
                <br>vvvvvvvvvvvvvvvvvvvvvvvvvvvv
                <h1>Template.DoesNotExist</h1>
                <br>slug={slug}
                <br>kit_of_templates={kit_of_templates}
                <br>kit_of_values={kit_of_values} 
                <br>^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """

    context = {
        "kit_of_templates": kit_of_templates,
        "kit_of_values": kit_of_values,
        "object": init_object,
        "global": global_context,
    }
    # print(init_object.tags.all())
    return my_template.render_template_context(context=context)
