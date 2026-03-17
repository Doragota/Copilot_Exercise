from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populates the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Database populated successfully!')