from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Label, Wallpaper


@admin.register(Label)
class LabelAdmin(ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'created_at')
    fields = ('name', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Wallpaper)
class WallpaperAdmin(ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    fields = ('title', 'image_path', 'labels', 'source_url', 'created_at')
    autocomplete_fields = ('labels',)
    readonly_fields = ('created_at',)
