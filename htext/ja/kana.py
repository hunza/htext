# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unicodedata

from .utils import force_text, aggregate_whitespace


__all__ = (
    'to_katakana',
    'to_hiragana',
    'to_katakana_seion',
    'to_hiragana_seion',
    'get_kana_group',
    'compare',
    'remove_ignorable_chars',
    'hard_normalize',
)


def to_katakana(value):
    return force_text(value).translate(HIRAGANA_TO_KATAKANA)


def to_hiragana(value):
    value = force_text(value)

    for kata, hira in KATAKANA_TO_HIRAGANA_EXCEPTIONS:
        value = value.replace(kata, hira)

    return value.translate(KATAKANA_TO_HIRAGANA)


def to_hiragana_seion(value):
    return force_text(value).translate(TO_HIRAGANA_SEION)


def to_katakana_seion(value):
    return force_text(value).translate(TO_KATAKANA_SEION)


def hard_normalize(value, ignores=""" '"・!?=.、。"""):
    converted_value = unicodedata.normalize('NFKC', value)
    converted_value = aggregate_whitespace(converted_value)
    converted_value = remove_ignorable_chars(converted_value, ignores).lower()
    converted_value = to_katakana(converted_value)
    converted_value = to_katakana_seion(converted_value)

    return converted_value


def _get_kana_group():
    _KANA_LIST = (
        (u"あ", u"ァアィイゥウェエォオヴ"),
        (u"か", u"カガキギクグケゲコゴヵヶ"),
        (u"さ", u"サザシジスズセゼソゾ"),
        (u"た", u"タダチヂッツヅテデトド"),
        (u"な", u"ナニヌネノ"),
        (u"は", u"ハバパヒビピフブプヘベペホボポ"),
        (u"ま", u"マミムメモ"),
        (u"や", u"ャヤュユョヨ"),
        (u"ら", u"ラリルレロ"),
        (u"わ", u"ヮワヰヱヲン"),
    )

    table = {}
    for v, chars in _KANA_LIST:
        for char in chars:
            table[char] = v

    def get_kana_group(value):
        if value:
            value = force_text(value)
            char = to_katakana(value[0])
            return table.get(char)
        else:
            return None
    return get_kana_group
get_kana_group = _get_kana_group()


def compare(first, second, ignores='・!！?？'):
    """
    >>> compare('アンジェラ・アキ', 'アンジェラアキ')
    0
    >>> compare('アイドリング!!!', 'アイドリング')
    0
    >>> compare('ゆず', 'ユズ')
    0
    """
    first = remove_ignorable_chars(first, ignores)
    second = remove_ignorable_chars(second, ignores)

    first_katakana = to_katakana(first)
    second_katakana = to_katakana(second)

    return cmp(first_katakana, second_katakana)


def remove_ignorable_chars(value, ignores=""" '"・!！?？=＝.、。"""):
    for c in (ignores):
        value = value.replace(c, '')
    return value


HIRAGANA_TO_KATAKANA = dict((k, v) for k, v in zip(range(ord(u"ぁ"), ord(u"ん") + 1),
                                                   range(ord(u"ァ"), ord(u"ン") + 1),
                                                   ))

KATAKANA_TO_HIRAGANA = dict((v, k) for k, v in HIRAGANA_TO_KATAKANA.items())

TO_HIRAGANA_SEION = dict((k, v) for k, v in zip(
    [ord(x) for x in ("がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"
                      "ぁぃぅぇぉっゃゅょゐゑ")],
    [ord(x) for x in ("かきくけこさしすせそたちつてとはひふへほはひふへほ"
                      "あいうえおつやゆよいえ")],
))

TO_KATAKANA_SEION = dict((k, v) for k, v in zip(
    [ord(x) for x in ("ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポヴ"
                      "ァィゥェォヵヶッャュョヮヰヱ")],
    [ord(x) for x in ("カキクケコサシスセソタチツテトハヒフヘホハヒフヘホウ"
                      "アイウエオカケツヤユヨワイエ")],
))

# special rules
KATAKANA_TO_HIRAGANA_EXCEPTIONS = [
    (u"ヴァ", u"ば"),
    (u"ヴィ", u"び"),
    (u"ヴェ", u"べ"),
    (u"ヴォ", u"ぼ"),
    (u"ヴ",   u"ブ"),
]
