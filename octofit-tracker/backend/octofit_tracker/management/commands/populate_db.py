from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populates the database with a test user'

    def handle(self, *args, **kwargs):
        # Definiáljuk a teszt adatokat
        VAR_USERNAME = 'mona_test'
        VAR_EMAIL = 'mona@example.com'
        
        # Ellenőrizzük, létezik-e már, ha nem, létrehozzuk
        if not User.objects.filter(username=VAR_USERNAME).exists():
            User.objects.create_user(VAR_USERNAME, VAR_EMAIL, 'password123')
            self.stdout.write(self.style.SUCCESS(f'Siker! Létrehozva a felhasználó: {VAR_USERNAME}'))
        else:
            self.stdout.write('A teszt felhasználó már korábban létrejött.')