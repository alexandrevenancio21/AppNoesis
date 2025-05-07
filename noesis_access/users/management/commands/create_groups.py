from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        roles = ['admin', 'developers', 'RH', 'comerciais', 'marketing', 'financeiro']
        for role in roles:
            Group.objects.get_or_create(name=role)
        self.stdout.write(self.style.SUCCESS('Grupos criados com sucesso.'))