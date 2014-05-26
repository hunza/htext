# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unicodedata

from .utils import force_text


__all__ = ('to_han', 'to_zen')


def to_zen(value):
    """
    Convert hankaku chars to zenkaku chars
    """
    value = force_text(value)
    normalized_value = unicodedata.normalize('NFKC', value)
    return normalized_value.translate(HAN_TO_ZEN_TABLE)


def to_han(value):
    """
    Convert zenkaku chars to hankaku chars
    """
    value = force_text(value)
    return value.translate(ZEN_TO_HAN_TABLE)


ZEN_TO_HAN_PAIRS = (
    # Fullwidth ASCII variants
    ("！", "!"),  # FF01 => 0021 FULLWIDTH EXCLAMATION MARK
    ("＂", "\""), # FF02 => 0022 FULLWIDTH QUOTATION MARK
    ("＃", "#"),  # FF03 => 0023 FULLWIDTH NUMBER SIGN
    ("＄", "$"),  # FF04 => 0024 FULLWIDTH DOLLAR SIGN
    ("％", "%"),  # FF05 => 0025 FULLWIDTH PERCENT SIGN
    ("＆", "&"),  # FF06 => 0026 FULLWIDTH AMPERSAND
    ("＇", "'"),  # FF07 => 0027 FULLWIDTH APOSTROPHE
    ("（", "("),  # FF08 => 0028 FULLWIDTH LEFT PARENTHESIS
    ("）", ")"),  # FF09 => 0029 FULLWIDTH RIGHT PARENTHESIS
    ("＊", "*"),  # FF0A => 002A FULLWIDTH ASTERISK
    ("＋", "+"),  # FF0B => 002B FULLWIDTH PLUS SIGN
    ("，", ","),  # FF0C => 002C FULLWIDTH COMMA
    ("－", "-"),  # FF0D => 002D FULLWIDTH HYPHEN-MINUS
    ("．", "."),  # FF0E => 002E FULLWIDTH FULL STOP
    ("／", "/"),  # FF0F => 002F FULLWIDTH SOLIDUS

    ("：", ":"),  # FF1A => 003A FULLWIDTH COLON
    ("；", ";"),  # FF1B => 003B FULLWIDTH SEMICOLON
    ("＜", "<"),  # FF1C => 003C FULLWIDTH LESS-THAN SIGN
    ("＝", "="),  # FF1D => 003D FULLWIDTH EQUALS SIGN
    ("＞", ">"),  # FF1E => 003E FULLWIDTH GREATER-THAN SIGN
    ("？", "?"),  # FF1F => 003F FULLWIDTH QUESTION MARK
    ("＠", "@"),  # FF20 => 0040 FULLWIDTH COMMERCIAL AT

    ("［", "["),  # FF3B => 005B FULLWIDTH LEFT SQUARE BRACKET
    ("＼", "\\"), # FF3C => 005C FULLWIDTH REVERSE SOLIDUS
    ("］", "]"),  # FF3D => 005D FULLWIDTH RIGHT SQUARE BRACKET
    ("＾", "^"),  # FF3E => 005E FULLWIDTH CIRCUMFLEX ACCENT
    ("＿", "_"),  # FF3F => 005F FULLWIDTH LOW LINE
    ("｀", "`"),  # FF40 => 0060 FULLWIDTH GRAVE ACCENT

    ("｛", "{"),  # FF5B => 007B FULLWIDTH LEFT CURLY BRACKET
    ("｜", "|"),  # FF5C => 007C FULLWIDTH VERTICAL LINE
    ("｝", "}"),  # FF5D => 007D FULLWIDTH RIGHT CURLY BRACKET
    ("～", "~"),  # FF5E => 007E FULLWIDTH TILDE

    ("０", "0"),  # FF10 => 0030 FULLWIDTH DIGIT ZERO
    ("１", "1"),  # FF11 => 0031 FULLWIDTH DIGIT ONE
    ("２", "2"),  # FF12 => 0032 FULLWIDTH DIGIT TWO
    ("３", "3"),  # FF13 => 0033 FULLWIDTH DIGIT THREE
    ("４", "4"),  # FF14 => 0034 FULLWIDTH DIGIT FOUR
    ("５", "5"),  # FF15 => 0035 FULLWIDTH DIGIT FIVE
    ("６", "6"),  # FF16 => 0036 FULLWIDTH DIGIT SIX
    ("７", "7"),  # FF17 => 0037 FULLWIDTH DIGIT SEVEN
    ("８", "8"),  # FF18 => 0038 FULLWIDTH DIGIT EIGHT
    ("９", "9"),  # FF19 => 0039 FULLWIDTH DIGIT NINE

    ("Ａ", "A"),  # FF21 => 0041 FULLWIDTH LATIN CAPITAL LETTER A
    ("Ｂ", "B"),  # FF22 => 0042 FULLWIDTH LATIN CAPITAL LETTER B
    ("Ｃ", "C"),  # FF23 => 0043 FULLWIDTH LATIN CAPITAL LETTER C
    ("Ｄ", "D"),  # FF24 => 0044 FULLWIDTH LATIN CAPITAL LETTER D
    ("Ｅ", "E"),  # FF25 => 0045 FULLWIDTH LATIN CAPITAL LETTER E
    ("Ｆ", "F"),  # FF26 => 0046 FULLWIDTH LATIN CAPITAL LETTER F
    ("Ｇ", "G"),  # FF27 => 0047 FULLWIDTH LATIN CAPITAL LETTER G
    ("Ｈ", "H"),  # FF28 => 0048 FULLWIDTH LATIN CAPITAL LETTER H
    ("Ｉ", "I"),  # FF29 => 0049 FULLWIDTH LATIN CAPITAL LETTER I
    ("Ｊ", "J"),  # FF2A => 004A FULLWIDTH LATIN CAPITAL LETTER J
    ("Ｋ", "K"),  # FF2B => 004B FULLWIDTH LATIN CAPITAL LETTER K
    ("Ｌ", "L"),  # FF2C => 004C FULLWIDTH LATIN CAPITAL LETTER L
    ("Ｍ", "M"),  # FF2D => 004D FULLWIDTH LATIN CAPITAL LETTER M
    ("Ｎ", "N"),  # FF2E => 004E FULLWIDTH LATIN CAPITAL LETTER N
    ("Ｏ", "O"),  # FF2F => 004F FULLWIDTH LATIN CAPITAL LETTER O
    ("Ｐ", "P"),  # FF30 => 0050 FULLWIDTH LATIN CAPITAL LETTER P
    ("Ｑ", "Q"),  # FF31 => 0051 FULLWIDTH LATIN CAPITAL LETTER Q
    ("Ｒ", "R"),  # FF32 => 0052 FULLWIDTH LATIN CAPITAL LETTER R
    ("Ｓ", "S"),  # FF33 => 0053 FULLWIDTH LATIN CAPITAL LETTER S
    ("Ｔ", "T"),  # FF34 => 0054 FULLWIDTH LATIN CAPITAL LETTER T
    ("Ｕ", "U"),  # FF35 => 0055 FULLWIDTH LATIN CAPITAL LETTER U
    ("Ｖ", "V"),  # FF36 => 0056 FULLWIDTH LATIN CAPITAL LETTER V
    ("Ｗ", "W"),  # FF37 => 0057 FULLWIDTH LATIN CAPITAL LETTER W
    ("Ｘ", "X"),  # FF38 => 0058 FULLWIDTH LATIN CAPITAL LETTER X
    ("Ｙ", "Y"),  # FF39 => 0059 FULLWIDTH LATIN CAPITAL LETTER Y
    ("Ｚ", "Z"),  # FF3A => 005A FULLWIDTH LATIN CAPITAL LETTER Z

    ("ａ", "a"),  # FF41 => 0061 FULLWIDTH LATIN SMALL LETTER A
    ("ｂ", "b"),  # FF42 => 0062 FULLWIDTH LATIN SMALL LETTER B
    ("ｃ", "c"),  # FF43 => 0063 FULLWIDTH LATIN SMALL LETTER C
    ("ｄ", "d"),  # FF44 => 0064 FULLWIDTH LATIN SMALL LETTER D
    ("ｅ", "e"),  # FF45 => 0065 FULLWIDTH LATIN SMALL LETTER E
    ("ｆ", "f"),  # FF46 => 0066 FULLWIDTH LATIN SMALL LETTER F
    ("ｇ", "g"),  # FF47 => 0067 FULLWIDTH LATIN SMALL LETTER G
    ("ｈ", "h"),  # FF48 => 0068 FULLWIDTH LATIN SMALL LETTER H
    ("ｉ", "i"),  # FF49 => 0069 FULLWIDTH LATIN SMALL LETTER I
    ("ｊ", "j"),  # FF4A => 006A FULLWIDTH LATIN SMALL LETTER J
    ("ｋ", "k"),  # FF4B => 006B FULLWIDTH LATIN SMALL LETTER K
    ("ｌ", "l"),  # FF4C => 006C FULLWIDTH LATIN SMALL LETTER L
    ("ｍ", "m"),  # FF4D => 006D FULLWIDTH LATIN SMALL LETTER M
    ("ｎ", "n"),  # FF4E => 006E FULLWIDTH LATIN SMALL LETTER N
    ("ｏ", "o"),  # FF4F => 006F FULLWIDTH LATIN SMALL LETTER O
    ("ｐ", "p"),  # FF50 => 0070 FULLWIDTH LATIN SMALL LETTER P
    ("ｑ", "q"),  # FF51 => 0071 FULLWIDTH LATIN SMALL LETTER Q
    ("ｒ", "r"),  # FF52 => 0072 FULLWIDTH LATIN SMALL LETTER R
    ("ｓ", "s"),  # FF53 => 0073 FULLWIDTH LATIN SMALL LETTER S
    ("ｔ", "t"),  # FF54 => 0074 FULLWIDTH LATIN SMALL LETTER T
    ("ｕ", "u"),  # FF55 => 0075 FULLWIDTH LATIN SMALL LETTER U
    ("ｖ", "v"),  # FF56 => 0076 FULLWIDTH LATIN SMALL LETTER V
    ("ｗ", "w"),  # FF57 => 0077 FULLWIDTH LATIN SMALL LETTER W
    ("ｘ", "x"),  # FF58 => 0078 FULLWIDTH LATIN SMALL LETTER X
    ("ｙ", "y"),  # FF59 => 0079 FULLWIDTH LATIN SMALL LETTER Y
    ("ｚ", "z"),  # FF5A => 007A FULLWIDTH LATIN SMALL LETTER Z

    # Halfwidth CJK punctuation
    ("。", "｡"),  # 3002 => FF61 IDEOGRAPHIC FULL STOP
    ("「", "｢"),  # 300C => FF62 LEFT CORNER BRACKET
    ("」", "｣"),  # 300D => FF63 RIGHT CORNER BRACKET
    ("、", "､"),  # 3001 => FF64 IDEOGRAPHIC COMMA

    # Fullwidth symbol variants
    ("￠", "¢"),  # FFE0 => 00A2 FULLWIDTH CENT SIGN
    ("￡", "£"),  # FFE1 => 00A3 FULLWIDTH POUND SIGN
    ("￢", "¬"),  # FFE2 => 00AC FULLWIDTH NOT SIGN
    ("￣", "¯"),  # FFE3 => 00AF FULLWIDTH MACRON
    ("￤", "¦"),  # FFE4 => 00A6 FULLWIDTH BROKEN BAR
    ("￥", "¥"),  # FFE5 => 00A5 FULLWIDTH YEN SIGN
    ("￦", "₩"),  # FFE6 => 20A9 FULLWIDTH WON SIGN

    # Halfwidth symbol variants
    ("│", "￨"),  # 2502 => FFE8 BOX DRAWINGS LIGHT VERTICAL
    ("←", "￩"),  # 2190 => FFE9 LEFTWARDS ARROW
    ("↑", "￪"),  # 2191 => FFEA UPWARDS ARROW
    ("→", "￫"),  # 2192 => FFEB RIGHTWARDS ARROW
    ("↓", "￬"),  # 2193 => FFEC DOWNWARDS ARROW
    ("■", "￭"),  # 25A0 => FFED BLACK SQUARE
    ("○", "￮"),  # 25CB => FFEE WHITE CIRCLE

    ## Katakana
    ('ァ', 'ｧ'),
    ('ア', 'ｱ'),
    ('ィ', 'ｨ'),
    ('イ', 'ｲ'),
    ('ゥ', 'ｩ'),
    ('ウ', 'ｳ'),
    ('ヴ', 'ｳﾞ'),
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

ZEN_TO_HAN_TABLE = dict((ord(z), h) for z, h in ZEN_TO_HAN_PAIRS)
HAN_TO_ZEN_TABLE = dict((ord(h), z) for z, h in ZEN_TO_HAN_PAIRS if len(h) == 1)
