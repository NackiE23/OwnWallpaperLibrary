# Generated by Django 5.1.7 on 2025-03-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='wallpaper',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='wallpaper',
            name='labels',
            field=models.ManyToManyField(related_name='wallpapers', to='wallpaper_library.label'),
        ),
        migrations.DeleteModel(
            name='WallpaperLabel',
        ),
    ]
