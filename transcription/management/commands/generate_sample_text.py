from django.core.management.base import BaseCommand

from transcription import sampletext
from transcription.models import Sentence


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        filepath = options['file']

        results = sampletext.generate_sample_text(filepath)

        Sentence.objects.bulk_create([
            Sentence(content=content) for content in results
        ])
