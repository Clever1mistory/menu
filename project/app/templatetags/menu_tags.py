from django import template
from app.models import MenuItem

register = template.Library()


@register.inclusion_tag('app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(parent=None)
    for item in menu_items:
        item.active = context['request'].path == item.get_url()
    return {'menu_items': menu_items}
