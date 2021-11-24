from django.db import models


class Entry(models.Model):
    content = models.CharField(max_length=256, db_index=True)
    arpabet_transcription = models.CharField(max_length=256)
    ipa_transcription = models.CharField(max_length=256)
    cz_transcription = models.CharField(max_length=256)
    ru_transcription = models.CharField(max_length=256)


class Sentence(models.Model):
    content = models.TextField()
