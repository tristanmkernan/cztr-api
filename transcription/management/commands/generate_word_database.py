from django.core.management.base import BaseCommand

from transcription import transcriber
from transcription.models import Entry

import nltk


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        dictionary = nltk.corpus.cmudict.dict()

        to_create = []

        for word, arpabet_transcription in dictionary.items():
            cz_transcription = transcriber.transcribe(word, lang='cz')

            to_create.append(
                Entry(
                    content=word,
                    arpabet_transcription=arpabet_transcription,
                    cz_transcription=cz_transcription
                )
            )

        Entry.objects.bulk_create(to_create)
