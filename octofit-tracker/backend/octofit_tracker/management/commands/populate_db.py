from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    # Ez a sor a kulcs, pontosan így kell írni:
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        VAR_USERNAME = 'mona_test'
        VAR_EMAIL = 'mona@example.com'
        
        if not User.objects.filter(username=VAR_USERNAME).exists():
            User.objects.create_user(VAR_USERNAME, VAR_EMAIL, 'password123')
            self.stdout.write(self.style.SUCCESS('Successfully populated test data!'))
        else:
            self.stdout.write('Test data already exists.')