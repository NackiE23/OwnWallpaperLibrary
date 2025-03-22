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
    list_display = ('title', 'label_list', 'created_at')
    search_fields = ('title',)
    fields = ('title', 'image_path', 'labels', 'source_url', 'created_at')
    autocomplete_fields = ('labels',)
    readonly_fields = ('created_at',)

    def label_list(self, obj):
        return ', '.join([label.name for label in obj.labels.all()])
    label_list.short_description = 'Labels'

    def get_queryset(self, request):
        # Optimize the query count
        return super().get_queryset(request).prefetch_related('labels')
