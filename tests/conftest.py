import pytest


from transcription.models import Entry, Sentence


@pytest.fixture
def seed_sentences(db):
    Sentence.objects.bulk_create([
        Sentence(content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
        Sentence(content='Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'),
        Sentence(content='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'),
        Sentence(content='Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    ])


@pytest.fixture
def seed_entries(db):
    Entry.objects.bulk_create([
        Entry(
            content='aardvark',
            arpabet_transcription='aa rd va rk',
            ipa_transcription='valid ipa transcription',
            cz_transcription='valid cz transcription'
        ),
        Entry(
            content='bat',
            arpabet_transcription='b a t',
            ipa_transcription='valid ipa transcription',
            cz_transcription='valid cz transcription'
        ),
        Entry(
            content='tiger',
            arpabet_transcription='t i g er',
            ipa_transcription='valid ipa transcription',
            cz_transcription='valid cz transcription'
        ),
    ])
