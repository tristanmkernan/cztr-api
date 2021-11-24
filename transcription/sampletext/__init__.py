"""
Potential optimizations: http://blog.behnel.de/posts/faster-xml-stream-processing-in-python.html
"""
from typing import List

import string
import lxml.etree as ET

import mwparserfromhell
import nltk

from nltk.tokenize import word_tokenize, sent_tokenize


arpabet = nltk.corpus.cmudict.dict()

arpabet_words = set(arpabet.keys())


def remove_punctuation(content: str) -> str:
    return content.translate(str.maketrans('', '', string.punctuation))


def parse_sentences(text: str) -> List[str]:
    parsed = sent_tokenize(text)

    return parsed


def acceptable_content(text: str):
    text = text.lower()

    text = remove_punctuation(text)

    words = word_tokenize(text)

    return len(words) > 4 and set(words).issubset(arpabet_words)


def generate_sample_text(file_path):
    results = []

    for event, elem in ET.iterparse(file_path, events=("end",), tag=('{http://www.mediawiki.org/xml/export-0.10/}page',)):

        title_elem = elem.find('{http://www.mediawiki.org/xml/export-0.10/}title')
        revision_elem = elem.find('{http://www.mediawiki.org/xml/export-0.10/}revision')
        text_elem = revision_elem.find('{http://www.mediawiki.org/xml/export-0.10/}text')

        if text_elem.text and '#redirect' not in text_elem.text:
            wikicode = mwparserfromhell.parse(text_elem.text)

            text = wikicode.strip_code()

            for sentence in parse_sentences(text):
                if acceptable_content(sentence):

                    results.append(sentence)

                    print(f'Found result - {sentence}')

            if len(results) > 1000:
                break

        elem.clear()

    return results
