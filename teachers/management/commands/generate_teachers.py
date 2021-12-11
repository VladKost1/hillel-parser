from django.core.management.base import BaseCommand, CommandError
from teachers.models import Teachers
from faker import Faker
from random import randint
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        a = Faker()
        for i in range(options.get('number')):
            teachers = Teachers.objects.create(first_name=a.first_name(), last_name=a.last_name(), age=randint(15, 70))
            logger.info(f'First name: {teachers.first_name}, Last name: {teachers.last_name}, Age: {teachers.age}')

