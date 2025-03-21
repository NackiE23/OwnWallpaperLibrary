from django.db import models
from django.utils.translation import gettext_lazy as _


class S3PathField(models.URLField):
    pass


class Label(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Wallpaper(models.Model):
    title = models.CharField(max_length=255)
    image_path = S3PathField()
    source_url = models.URLField(null=True, blank=True, help_text=_('URL to the original source of the wallpaper'))
    labels = models.ManyToManyField(Label, related_name='wallpapers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
