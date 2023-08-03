from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'This is my custom command.'

    def handle(self, *args, **options):
        self.stdout.write('My custom command is running!')