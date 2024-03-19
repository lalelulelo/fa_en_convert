"""
From Reza Kamalifard persian.py with the mappings reviewed.
Reza Kamalifard (mrkamalifard@gmail.com - @rezakamalifard - https://github.com/itmard/Persian
"""


import re
import urllib.parse


def convert_en_numbers(input_str):
    """
    Converts English numbers to Persian numbers
    """
    mapping = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }
    return _multiple_replace(mapping, input_str)

def convert_en_characters(input_str):
    """
    Converts English characters to Persian characters
    """
    mapping = {
        'a': 'ا',
        'b': 'ب',
        'c': 'c',
        'd': 'د',
        'e': 'e',
        'f': 'ف',
        'g': 'گ',
        'h': 'ه',
        'i': 'ی',
        'j': 'ژ',
        'k': 'ک',
        'l': 'ل',
        'm': 'م',
        'n': 'ن',
        'o': 'و',
        'p': 'پ',
        'q': 'ک',
        'r': 'ر',
        's': 'س',
        't': 'ت',
        'u': 'و',
        'v': 'و',
        'w': 'و',
        'y': 'y',
        'z': 'ز',
        '?': '؟',
    }
    return _multiple_replace(mapping, input_str)

def convert_fa_numbers(input_str):
    """
    Converts Persian numbers to English numbers
    """
    mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
    }
    return _multiple_replace(mapping, input_str)

def convert_fa_characters(input_str):
    """
    Converts Persian characters to English characters
    """
    mapping = {
        'آ': 'aa',
        'ا': 'a',
        'ب': 'b',
        'پ': 'p',
        'ت': 't',
        'ث': 's',
        'ج': 'dj',
        'چ': 'tsh',
        'ح': 'h',
        'خ': 'kh',
        'د': 'd',
        'ذ': 'z',
        'ر': 'r',
        'ز': 'z',
        'ژ': 'j',
        'س': 's',
        'ش': 'sh',
        'ص': 'ss',
        'ض': 'zz',
        'ط': 't',
        'ظ': 'zzz',
        'ع': '`',
        'غ': 'gh',
        'ف': 'f',
        'ق': 'q',
        'ک': 'k',
        'گ': 'g',
        'ل': 'l',
        'م': 'm',
        'ن': 'n',
        'و': 'v',
        'ه': 'h',
        'ی': 'i',
        '؟': '?',
    }
    return _multiple_replace(mapping, input_str)

def convert_fa_spaces(input_value: str) -> str:
    """
    Convert space between Persian MI and De-Yii to zero-width non-joiner (halfspace) char
    :param input_value: String contains persian chars
    :return: New string with converted space to half space char
    """

    # u200C is the code for unicode zwnj character https://en.wikipedia.org/wiki/Zero-width_non-joiner
    repl = '\\2\u200C\\4'
    # replace space between persian MI.
    mi_pattern = r'((\s\u0645\u06CC)+([\s])+([\u0600-\u06EF]{1,}){1,})'
    result = re.sub(mi_pattern, repl, input_value, 0)
    # replace space between persian De-Yii.
    de_yii_pattern = r'(([\u0600-\u06EF]{1,})+([\s])+(ای|ایی|اند|ایم|اید|ام){1})'
    result = re.sub(de_yii_pattern, repl, result)

    return result

def decode_url(input_str):
    """
    Decode Persian charachters in URL
    :param input_str: String contains encoded URL
    :return: New string with decoded URL
    """
    return urllib.parse.unquote(input_str)

def _multiple_replace(mapping, text):
    """
    Internal function for replace all mapping keys for a input string
    :param mapping: replacing mapping keys
    :param text: user input string
    :return: New string with converted mapping keys to values
    """
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))


print(convert_fa_characters('سرلشکر باقری'))