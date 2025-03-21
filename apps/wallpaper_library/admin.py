from typing import Any

from django.contrib import admin
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin

from .models import Label, Wallpaper


@admin.register(Label)
class LabelAdmin(ModelAdmin):
    search_fields = ('name',)


@admin.register(Wallpaper)
class WallpaperAdmin(ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    fields = ('title', 'image_path', 'labels', 'source_url', 'created_at')
    autocomplete_fields = ('labels',)
    readonly_fields = ('created_at',)
