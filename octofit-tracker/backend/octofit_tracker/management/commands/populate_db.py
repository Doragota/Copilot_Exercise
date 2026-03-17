from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populates the database'

    def handle(self, *args, **kwargs):
        # Létrehozunk egy teszt felhasználót, ha még nem létezik
        if not User.objects.filter(username='mona').exists():
            User.objects.create_user('mona', 'mona@octocat.com', 'password123')
            self.stdout.write(self.style.SUCCESS('User mona created successfully!'))
        else:
            self.stdout.write('User mona already exists.')