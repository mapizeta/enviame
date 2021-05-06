from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        from django.core import management
        from django.core.management.commands import loaddata
    
        management.call_command('loaddata', 'empresas.json', verbosity=0)