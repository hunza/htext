# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import six

from htext.ja import kana

DATA = [
    ("コーリャ", "こーりゃ"),
    ("アレクセイ・カラマーゾフ", "あれくせい・からまーぞふ"),
    ]

def test_invalid():
    def func(input, expected):
        output = kana.to_hiragana(input)
        assert isinstance(output, six.text_type) and output == expected

        output = kana.to_katakana(input)
        assert isinstance(output, six.text_type) and output == expected

        output = kana.to_zen(input)
        assert isinstance(output, six.text_type) and output == expected, output

        output = kana.to_han(input)
        assert isinstance(output, six.text_type) and output == expected

    # not unicode
    for input, expected in (
            (1, '1'),
            (1.0, '1.0'),
            ('A', 'A'),
            (None, 'None')):
        yield func, input, expected

    # Neigther hiragana nor katakana
    for input in ("酒", "\u2200"):
        yield func, input, input

def test_to_hiragana():
    def func(input, expected):
        output = kana.to_hiragana(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for i, e in DATA + [("ドウモト", "どうもと"),
                        ("ヴァスティッチ", "ばすてぃっち"),
                        ("イブラヒモヴィッチ", "いぶらひもびっち"),
                        ("ヴェンゲル", "べんげる"),
                        ("クリエイティヴ", "くりえいてぃぶ"),
                        ]:
        yield func, i, e

def test_to_katakana():
    def func(input, expected):
        output = kana.to_katakana(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for e, i in DATA + [("ドウモト", "どうもと"),
                        ("バスティッチ", "ばすてぃっち"),
                        ("イブラヒモビッチ", "いぶらひもびっち"),
                        ("ベンゲル", "べんげる"),
                        ]:
        yield func, i, e

def test_hiragana_to_katakana_unchanged():
    def func(input, expected):
        output = kana.to_katakana(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for e, i in DATA:
        yield func, e, e

def test_katakana_to_hiragana_unchanged():
    def func(input, expected):
        output = kana.to_hiragana(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for e, i in DATA:
        yield func, i, i

def test_mixed():
    output = kana.to_hiragana("カラマーゾフの兄弟")
    assert output == "からまーぞふの兄弟"

    output = kana.to_katakana("からまーぞふの兄弟")
    assert output == "カラマーゾフノ兄弟"

def test_row():
    def func(input, expected):
        output = kana.get_kana_row(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for input, expected in (("アリョーシャ", "あ"),
                            ("コーリャ", "か"),
                            ("サムソーノフ", "さ"),
                            ("タチアナ", "た"),
                            ("ナスターシャ", "な"),
                            ("フィリッポーヴナ", "は"),
                            ("ミーチャ", "ま"),
                            ("ユヴゲーニ・パーベルビチ", "や"),
                            ("ポルフィーリ ペトロヴィッチ", "は"),
                            ):
        yield func, input, expected
