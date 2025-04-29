from django.core.management import BaseCommand

from apps.wallpaper_library.utils import import_wallpapers_from_s3


class Command(BaseCommand):
    help = 'Import wallpapers from S3'

    def handle(self, *args, **options):
        """
        Import wallpapers from S3.
        """
        success_count = import_wallpapers_from_s3()
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {success_count} wallpapers from S3'))
