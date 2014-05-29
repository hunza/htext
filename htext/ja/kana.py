# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .utils import force_text


__all__ = ('to_katakana', 'to_hiragana', 'get_kana_group', 'compare', 'remove_ignorable_chars')


def to_katakana(value):
    return force_text(value).translate(HIRAGANA_TO_KATAKANA)


def to_hiragana(value):
    value = force_text(value)

    for kata, hira in KATAKANA_TO_HIRAGANA_EXCEPTIONS:
        value = value.replace(kata, hira)

    return value.translate(KATAKANA_TO_HIRAGANA)


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


HIRAGANA_TO_KATAKANA = dict((k, v) for k, v in zip(range(ord(u"ぁ"), ord(u"ん")+1),
                                                   range(ord(u"ァ"), ord(u"ン")+1),
                                                   ))
KATAKANA_TO_HIRAGANA = dict((v, k) for k, v in HIRAGANA_TO_KATAKANA.items())

# special rules
KATAKANA_TO_HIRAGANA_EXCEPTIONS = [
    (u"ヴァ", u"ば"),
    (u"ヴィ", u"び"),
    (u"ヴェ", u"べ"),
    (u"ヴォ", u"ぼ"),
    (u"ヴ",   u"ブ"),
]
