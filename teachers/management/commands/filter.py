from django.core.management.base import BaseCommand, CommandError
from teachers.models import Teachers

import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--first_name', type=str)
        parser.add_argument('--last_name', type=str)
        parser.add_argument('--age', type=int)

    def handle(self, *args, **options):
        teachers = Teachers.objects.all()
        if options.get('first_name'):
            teachers = teachers.filter(first_name=options.get('first_name'))
        if options.get('last_name'):
            teachers = teachers.filter(last_name=options.get('last_name'))
        if options.get('age'):
            teachers = teachers.filter(age=options.get('age'))
        logger.info(teachers)
