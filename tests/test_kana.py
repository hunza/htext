# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from htext.ja import kana

DATA = [
    (u"コーリャ", u"こーりゃ"),
    (u"アレクセイ・カラマーゾフ", u"あれくせい・からまーぞふ"),
    ]

def test_invalid():
    def func(input, expected):
        output = kana.to_hiragana(input)
        assert isinstance(output, unicode) and output == expected

        output = kana.to_katakana(input)
        assert isinstance(output, unicode) and output == expected

        output = kana.to_zen(input)
        assert isinstance(output, unicode) and output == expected, output

        output = kana.to_han(input)
        assert isinstance(output, unicode) and output == expected

    # not unicode
    for input in (1, 1.0, 'A', None):
        yield func, input, unicode(input)

    # Neigther hiragana nor katakana
    for input in (u"酒", u"\u2200"):
        yield func, input, input

def test_to_hiragana():
    def func(input, expected):
        output = kana.to_hiragana(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for i, e in DATA + [(u"ドウモト", u"どうもと"),
                        (u"ヴァスティッチ", u"ばすてぃっち"),
                        (u"イブラヒモヴィッチ", u"いぶらひもびっち"),
                        (u"ヴェンゲル", u"べんげる"),
                        (u"クリエイティヴ", u"くりえいてぃぶ"),
                        ]:
        yield func, i, e

def test_to_katakana():
    def func(input, expected):
        output = kana.to_katakana(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for e, i in DATA + [(u"ドウモト", u"どうもと"),
                        (u"バスティッチ", u"ばすてぃっち"),
                        (u"イブラヒモビッチ", u"いぶらひもびっち"),
                        (u"ベンゲル", u"べんげる"),
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
    output = kana.to_hiragana(u"カラマーゾフの兄弟")
    assert output == u"からまーぞふの兄弟"

    output = kana.to_katakana(u"からまーぞふの兄弟")
    assert output == u"カラマーゾフノ兄弟"

def test_row():
    def func(input, expected):
        output = kana.get_kana_row(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for input, expected in ((u"アリョーシャ", u"あ"),
                            (u"コーリャ", u"か"),
                            (u"サムソーノフ", u"さ"),
                            (u"タチアナ", u"た"),
                            (u"ナスターシャ", u"な"),
                            (u"フィリッポーヴナ", u"は"),
                            (u"ミーチャ", u"ま"),
                            (u"ユヴゲーニ・パーベルビチ", u"や"),
                            (u"ポルフィーリ ペトロヴィッチ", u"は"),
                            ):
        yield func, input, expected
