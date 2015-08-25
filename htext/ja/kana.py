# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unicodedata

from .utils import force_text, aggregate_whitespace


IGNORABLE_CHARS = """ '"・!?=.、。"""


__all__ = (
    'to_katakana',
    'to_hiragana',
    'to_katakana_seion',
    'to_hiragana_seion',
    'get_kana_group',
    'compare',
    'remove_ignorable_chars',
    'soft_normalize',
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


def soft_normalize(value, ignores=IGNORABLE_CHARS, whitespace=True):
    """
    検索用に日本語文字列を正規化する
      - NFKCで変換
      - 記号や空白を除去
      - ひらがなをカタカナに強制
    """
    # ユニコードをNFKCで正規化する
    value = unicodedata.normalize('NFKC', value)

    # 不要な文字を削除
    value = remove_ignorable_chars(value, ignores=ignores)

    # 空白文字を正規化
    value = aggregate_whitespace(value)

    # 空白文字を除去
    if not whitespace:
        value = value.replace(' ', '')

    # カタカナに強制
    value = to_katakana(value)

    return value


def hard_normalize(value, ignores=IGNORABLE_CHARS, whitespace=False):
    """
    soft_normalizeに加えて以下の正規化を適用
      - カタカナ濁音を清音に強制
      - アルファベットを小文字に強制
    """
    value = soft_normalize(value, ignores=ignores, whitespace=whitespace)

    # カタカナ濁音をカタカナ清音に強制
    value = to_katakana_seion(value)

    # アルファベットを小文字に強制
    value = value.lower()

    return value


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
