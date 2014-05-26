# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unicodedata
import six

__all__ = ['to_katakana', 'to_hiragana', 'to_han', 'to_zen', 'get_kana_group']

def force_text(value):
    if isinstance(value, six.text_type):
        return value
    elif isinstance(value, six.string_types):
        return six.b(value).decode()
    else:
        value = str(value)
        return value if isinstance(value, six.text_type) else value.decode()

def to_katakana(value):
    return force_text(value).translate(HIRAGANA_TO_KATAKANA)

def to_hiragana(value):
    value = force_text(value)

    for kata, hira in KATAKANA_TO_HIRAGANA_EXCEPTIONS:
        value = value.replace(kata, hira)

    return value.translate(KATAKANA_TO_HIRAGANA)

def to_zen(value):
    """
    Convert hankaku-katakana to zenkaku katakana
    """
    value = force_text(value)
    return unicodedata.normalize('NFKC', value)

def to_han(value):
    """
    Convert zenkaku-katakana to hankaku katakana
    """
    value = force_text(value)
    return value.translate(ZEN_TO_HAN_TABLE)

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
        value = force_text(value)
        char = to_katakana(value[0])
        return table.get(char)
    return get_kana_group
get_kana_group = _get_kana_group()

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

KATAKANA_LIST = (
    ('ァ', 'ｧ'),
    ('ア', 'ｱ'),
    ('ィ', 'ｨ'),
    ('イ', 'ｲ'),
    ('ゥ', 'ｩ'),
    ('ウ', 'ｳ'),
    ('ェ', 'ｪ'),
    ('エ', 'ｴ'),
    ('ォ', 'ｫ'),
    ('オ', 'ｵ'),
    ('カ', 'ｶ'),
    ('ガ', 'ｶﾞ'),
    ('キ', 'ｷ'),
    ('ギ', 'ｷﾞ'),
    ('ク', 'ｸ'),
    ('グ', 'ｸﾞ'),
    ('ケ', 'ｹ'),
    ('ゲ', 'ｹﾞ'),
    ('コ', 'ｺ'),
    ('ゴ', 'ｺﾞ'),
    ('サ', 'ｻ'),
    ('ザ', 'ｻﾞ'),
    ('シ', 'ｼ'),
    ('ジ', 'ｼﾞ'),
    ('ス', 'ｽ'),
    ('ズ', 'ｽﾞ'),
    ('セ', 'ｾ'),
    ('ゼ', 'ｾﾞ'),
    ('ソ', 'ｿ'),
    ('ゾ', 'ｿﾞ'),
    ('タ', 'ﾀ'),
    ('ダ', 'ﾀﾞ'),
    ('チ', 'ﾁ'),
    ('ヂ', 'ﾁﾞ'),
    ('ッ', 'ｯ'),
    ('ツ', 'ﾂ'),
    ('ヅ', 'ﾂﾞ'),
    ('テ', 'ﾃ'),
    ('デ', 'ﾃﾞ'),
    ('ト', 'ﾄ'),
    ('ド', 'ﾄﾞ'),
    ('ナ', 'ﾅ'),
    ('ニ', 'ﾆ'),
    ('ヌ', 'ﾇ'),
    ('ネ', 'ﾈ'),
    ('ノ', 'ﾉ'),
    ('ハ', 'ﾊ'),
    ('バ', 'ﾊﾞ'),
    ('パ', 'ﾊﾟ'),
    ('ヒ', 'ﾋ'),
    ('ビ', 'ﾋﾞ'),
    ('ピ', 'ﾋﾟ'),
    ('フ', 'ﾌ'),
    ('ブ', 'ﾌﾞ'),
    ('プ', 'ﾌﾟ'),
    ('ヘ', 'ﾍ'),
    ('ベ', 'ﾍﾞ'),
    ('ペ', 'ﾍﾟ'),
    ('ホ', 'ﾎ'),
    ('ボ', 'ﾎﾞ'),
    ('ポ', 'ﾎﾟ'),
    ('マ', 'ﾏ'),
    ('ミ', 'ﾐ'),
    ('ム', 'ﾑ'),
    ('メ', 'ﾒ'),
    ('モ', 'ﾓ'),
    ('ャ', 'ｬ'),
    ('ヤ', 'ﾔ'),
    ('ュ', 'ｭ'),
    ('ユ', 'ﾕ'),
    ('ョ', 'ｮ'),
    ('ヨ', 'ﾖ'),
    ('ラ', 'ﾗ'),
    ('リ', 'ﾘ'),
    ('ル', 'ﾙ'),
    ('レ', 'ﾚ'),
    ('ロ', 'ﾛ'),
    ('ヮ', 'ﾜ'),
    ('ワ', 'ﾜ'),
    ('ヲ', 'ｦ'),
    ('ン', 'ﾝ'),
    ('ー', 'ｰ'),
    ('、', '､'),
    ('。', '｡'),
    ('・', '･'),
)

ZEN_TO_HAN_TABLE = dict((ord(z), h) for z, h in KATAKANA_LIST)
HAN_TO_ZEN_TABLE = dict((h, z) for z, h in KATAKANA_LIST)
