from django.urls import path

from apps.wallpaper_library.views import index_view


urlpatterns = [
    path('', index_view, name='index'),
]
