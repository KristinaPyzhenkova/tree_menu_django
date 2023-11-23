from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from app import models


def menu_view(request, menu_path):
    current_menu = None
    if not menu_path:
        return render(request, 'main.html', {'menu': current_menu})
    menu_names = menu_path.split('/')
    for menu_name in menu_names:
        current_menu = get_object_or_404(models.MenuItem, parent=current_menu, url=menu_name)
    return render(request, 'main.html', {'menu': current_menu})
