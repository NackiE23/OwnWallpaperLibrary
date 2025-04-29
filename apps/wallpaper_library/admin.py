from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from unfold.admin import ModelAdmin
from unfold.decorators import action

from .models import Label, Wallpaper
from .utils import import_wallpapers_from_s3


@admin.register(Label)
class LabelAdmin(ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'created_at')
    fields = ('name', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Wallpaper)
class WallpaperAdmin(ModelAdmin):
    list_display = ('title', 'label_list', 'created_at')
    search_fields = ('title',)
    fields = ('title', 'image_path', 'labels', 'source_url', 'created_at')
    autocomplete_fields = ('labels',)
    readonly_fields = ('created_at',)

    actions_list = ["sync_wallpapers_action"]

    @action(description=_("Sync wallpapers from s3"), url_path="sync-wallpapers-action")
    def sync_wallpapers_action(self, request: HttpRequest):
        success_count = import_wallpapers_from_s3()
        self.message_user(request, f"Successfully synced {success_count} wallpapers from S3.")
        return redirect(reverse_lazy('admin:wallpaper_library_wallpaper_changelist'))

    def label_list(self, obj):
        return ', '.join([label.name for label in obj.labels.all()])
    label_list.short_description = 'Labels'

    def get_queryset(self, request):
        # Optimize the query count
        return super().get_queryset(request).prefetch_related('labels')
