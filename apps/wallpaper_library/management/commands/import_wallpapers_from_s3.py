from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Import wallpapers from S3'

    def handle(self, *args, **options):
        # TODO: Implement importing wallpapers from S3
        success_count = 0
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {success_count} wallpapers from S3'))
