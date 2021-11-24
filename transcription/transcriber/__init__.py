"""
Resources

- https://stackoverflow.com/questions/33666557/get-phonemes-from-any-word-in-python-nltk-or-other-modules
- http://www.speech.cs.cmu.edu/cgi-bin/cmudict
- https://github.com/numediart/MBROLA-voices/tree/master/data/en1
- https://en.wikipedia.org/wiki/SAMPA
- https://www.phon.ucl.ac.uk/home/sampa/index.html
- https://github.com/ypeels/nltk-book/blob/master/exercises/2.21-syllable-count.py
- https://github.com/wwesantos/arpabet-to-ipa
- http://www.cs.columbia.edu/~julia/courses/CS6998-2019/%5B07%5D%20Phonetics.pdf
- http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=A844AD91A84613F31176FF1441EB79BF?doi=10.1.1.468.4065&rep=rep1&type=pdf
- https://www.u-aizu.ac.jp/~wilson/publications/NakatsukaNogitaWilson2020ETLTC.pdf
  - Research paper explaining similar goals
- https://github.com/cmusphinx/cmudict-tools
- https://pythonprogramming.net/wordnet-nltk-tutorial/
"""
import string

import nltk

from nltk.tokenize import word_tokenize

from .lang.cz import ipa_to_czech
from .lang.ru import ipa_to_russian_cyrillic


arpabet = nltk.corpus.cmudict.dict()


def remove_punctuation(content: str) -> str:
    return content.translate(str.maketrans('', '', string.punctuation))


def to_arpabet_phonemes(word):
    return arpabet.get(word, [])


def arpabet_to_ipa_phoneme(arpabet_token):
    convertionTable = {
        'AO': 'ɔ',
        'AO0': 'ɔ',
        'AO1': 'ɔ',
        'AO2': 'ɔ',
        'AA': 'ɑ',
        'AA0': 'ɑ',
        'AA1': 'ɑ',
        'AA2': 'ɑ',
        'IY': 'i',
        'IY0': 'i',
        'IY1': 'i',
        'IY2': 'i',
        'UW': 'u',
        'UW0': 'u',
        'UW1': 'u',
        'UW2': 'u',
        'EH': 'e',
        'EH0': 'e',
        'EH1': 'e',
        'EH2': 'e',
        'IH': 'ɪ',
        'IH0': 'ɪ',
        'IH1': 'ɪ',
        'IH2': 'ɪ',
        'UH': 'ʊ',
        'UH0': 'ʊ',
        'UH1': 'ʊ',
        'UH2': 'ʊ',
        'AH': 'ʌ',
        'AH0': 'ə',
        'AH1': 'ʌ',
        'AH2': 'ʌ',
        'AE': 'æ',
        'AE0': 'æ',
        'AE1': 'æ',
        'AE2': 'æ',
        'AX': 'ə',
        'AX0': 'ə',
        'AX1': 'ə',
        'AX2': 'ə',
        'EY': 'eɪ',
        'EY0': 'eɪ',
        'EY1': 'eɪ',
        'EY2': 'eɪ',
        'AY': 'aɪ',
        'AY0': 'aɪ',
        'AY1': 'aɪ',
        'AY2': 'aɪ',
        'OW': 'oʊ',
        'OW0': 'oʊ',
        'OW1': 'oʊ',
        'OW2': 'oʊ',
        'AW': 'aʊ',
        'AW0': 'aʊ',
        'AW1': 'aʊ',
        'AW2': 'aʊ',
        'OY': 'ɔɪ',
        'OY0': 'ɔɪ',
        'OY1': 'ɔɪ',
        'OY2': 'ɔɪ',
        'P': 'p',
        'B': 'b',
        'T': 't',
        'D': 'd',
        'K': 'k',
        'G': 'g',
        'CH': 'tʃ',
        'JH': 'dʒ',
        'F': 'f',
        'V': 'v',
        'TH': 'θ',
        'DH': 'ð',
        'S': 's',
        'Z': 'z',
        'SH': 'ʃ',
        'ZH': 'ʒ',
        'HH': 'h',
        'M': 'm',
        'N': 'n',
        'NG': 'ŋ',
        'L': 'l',
        'R': 'r',
        'ER': 'ɜr',
        'ER0': 'ɜr',
        'ER1': 'ɜr',
        'ER2': 'ɜr',
        'AXR': 'ər',
        'AXR0': 'ər',
        'AXR1': 'ər',
        'AXR2': 'ər',
        'W': 'w',
        'Y': 'j',
        ' ': ' '
    }
    return convertionTable[arpabet_token]


def transcribe(content: str, lang = 'cz') -> str:
    lang_algo = {
        'cz': ipa_to_czech,
        'ru': ipa_to_russian_cyrillic
    }[lang]

    content = content.lower()

    content = remove_punctuation(content)

    words = word_tokenize(content)

    output = ''

    for word in words:
        arpabet_tokens_list = to_arpabet_phonemes(word)

        # assume take first pronunciation available
        arpabet_tokens = next(iter(arpabet_tokens_list), [])

        ipa_tokens = [arpabet_to_ipa_phoneme(token) for token in arpabet_tokens]
        transcript = [lang_algo(token) for token in ipa_tokens]

        output += ''.join(transcript)
        output += ' '

    return output
