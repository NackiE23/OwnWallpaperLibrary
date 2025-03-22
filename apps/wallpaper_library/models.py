from django.db import models
from django.db.models.fields.files import FieldFile
from django.utils.translation import gettext_lazy as _

from config.settings import AWS_S3_URL


class S3Path(FieldFile):
    # TODO: Implement the S3Path class
    @property
    def path(self):
        return self.name

    @property
    def url(self):
        return f"{AWS_S3_URL}/{self.name}"


class S3Field(models.FileField):
    # TODO: Implement the S3Field class
    attr_class = S3Path


class Label(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Wallpaper(models.Model):
    title = models.CharField(max_length=255)
    image_path = S3Field()
    source_url = models.URLField(null=True, blank=True, help_text=_('URL to the original source of the wallpaper'))
    labels = models.ManyToManyField(Label, related_name='wallpapers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
