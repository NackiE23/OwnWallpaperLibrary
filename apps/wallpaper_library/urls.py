from django.urls import path

from apps.wallpaper_library.views import index_view, get_wallpaper_list_by_label


urlpatterns = [
    path('', index_view, name='index'),
    path('wallpaper_list/label-<int:label_pk>/', get_wallpaper_list_by_label, name='get_wallpaper_list_by_label'),
]
