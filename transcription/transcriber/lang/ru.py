

def ipa_to_russian_cyrillic(ipa_token):
    convertionTable = {
        'ɔ': 'а',
        'ɑ': 'а',
        'i': 'и',
        'u': 'у́',
        'e': 'э',
        'ɪ': 'и',
        'ʊ': 'у',
        'ʌ': 'ир',
        'ə': 'э',
        'æ': 'а',
        'eɪ': 'эи',
        'aɪ': 'ай',
        'oʊ': 'о',
        'aʊ': '',
        'ɔɪ': '',
        'p': 'п',
        'b': 'б',
        't': 'т',
        'd': 'д',
        'k': 'к',
        'g': 'г',
        'tʃ': 'ч',
        'dʒ': 'Дж',
        'f': 'ф',
        'v': 'в',
        'θ': 'ё',
        'ð': '',
        's': 'с',
        'z': 'з',
        'ʃ': 'ш',
        'ʒ': 'Ж',
        'h': '',
        'm': 'м',
        'n': 'н',
        'ŋ': '',
        'l': 'л',
        'r': 'р',
        'ɜr': '',
        'ər': '',
        'w': '',
        'j': 'j',
        ' ': ' ',
    }
    return convertionTable[ipa_token]
