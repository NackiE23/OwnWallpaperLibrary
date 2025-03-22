from django.core.management import BaseCommand

from apps.wallpaper_library.models import Label, Wallpaper
from utils.aws import S3Client


class Command(BaseCommand):
    help = 'Import wallpapers from S3'

    def handle(self, *args, **options):
        """
        Import wallpapers from S3.
        """
        s3 = S3Client()
        self._ensure_labels(s3)
        success_count = self._process_wallpapers(s3)
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {success_count} wallpapers from S3'))

    @staticmethod
    def _ensure_labels(s3: S3Client):
        """
        Ensure that all top-level folders in the S3 bucket are present as labels in the database.
        """
        top_level_folders = s3.get_top_level_folders()
        folder_names = [folder.split("/")[0] for folder in top_level_folders]

        for folder_name in folder_names:
            Label.objects.get_or_create(name=folder_name)

    @staticmethod
    def _process_wallpapers(s3: S3Client) -> int:
        """
        Process all wallpapers in the S3 bucket.
        """
        success_count = 0
        paginator = s3.get_client().get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=s3._bucket):
            for content in page.get('Contents', []):
                image_path = content['Key']
                if not image_path.endswith('/'):
                    label_name = image_path.split('/')[0]
                    wallpaper, _ = Wallpaper.objects.get_or_create(
                        image_path=image_path,
                        title=image_path.split('/')[-1]
                    )
                    wallpaper.labels.add(Label.objects.get(name=label_name))
                    success_count += 1

        return success_count
