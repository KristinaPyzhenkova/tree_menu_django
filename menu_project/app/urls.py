from django.urls import path
from app.views import menu_view

urlpatterns = [
    path('<path:menu_path>/', menu_view, name='menu_view'),
]