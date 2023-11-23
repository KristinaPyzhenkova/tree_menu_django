from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from django.urls import reverse

from app import models

register = template.Library()


@register.simple_tag
def draw_menu(request):
    current_path = request.resolver_match.kwargs.get('menu_path', 'menu')
    all_menus = models.MenuItem.objects.select_related('parent').prefetch_related('children').all()

    current_menu = None
    parent_menu = None
    menu_names = current_path.split('/')

    for menu_name in menu_names:
        parent_menu = current_menu
        current_menu = get_object_or_404(all_menus, parent=current_menu, url=menu_name)

    pre_parent = parent_menu.parent if parent_menu else None
    menu = all_menus.filter(parent=pre_parent)
    return mark_safe(render_menu(current_path, menu, current_menu))


def render_menu(current_path, menu, active_menu):
    result = f'<ul>'

    for child in menu:
        result += '<li'
        new_path = f"{current_path}/{child.url}" if current_path and current_path != child.url else child.url

        if active_menu.parent is None and active_menu in menu:
            split_path = new_path.split('/')
            new_path = '/'.join(split_path[:-3] + split_path[-1:])
        if active_menu.parent in menu and child in menu:
            split_path = new_path.split('/')
            new_path = '/'.join(split_path[:-3] + split_path[-1:])

        if child == active_menu:
            result += ' class="active"'
            result += f'><a>{child.title}</a>'
        else:
            result += f'><a href="{reverse("menu_view", kwargs={"menu_path": new_path})}">{child.title}</a>'

        children = getattr(child, 'children', []).all()
        if child == active_menu or any(c.id == active_menu.id for c in children):
            result += render_menu(new_path, children, active_menu)

        result += '</li>'

    result += '</ul>'
    return result
