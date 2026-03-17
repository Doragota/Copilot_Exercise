from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **kwargs):
        # VAR-os megoldás a sikerélményért
        VAR_USERNAME = 'mona_test'
        VAR_EMAIL = 'mona@example.com'
        
        if not User.objects.filter(username=VAR_USERNAME).exists():
            User.objects.create_user(VAR_USERNAME, VAR_EMAIL, 'password123')
            self.stdout.write(self.style.SUCCESS(f'Siker! Létrehozva: {VAR_USERNAME}'))
        else:
            self.stdout.write('A teszt felhasználó már létezik.')