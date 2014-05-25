# -*- coding: utf-8 -*-
from htext.ja import kana

DATA = [
    (u"コーリャ", u"ｺｰﾘｬ"),
    (u"ペレズヴォン", u"ﾍﾟﾚｽﾞｳﾞｫﾝ"),
    (u"アレクセイ・カラマーゾフ", u"ｱﾚｸｾｲ･ｶﾗﾏｰｿﾞﾌ"),
    (u"「スコトプリゴニエフスク」", u"｢ｽｺﾄﾌﾟﾘｺﾞﾆｴﾌｽｸ｣"),
    (u"。", u"｡")
    ]

def test_han_to_zen():
    def func(input, expected):
        output = kana.to_zen(input)
        assert output, "%r expected, got %r" % (expected, output)

    for i, e in DATA:
        yield func, i, e

    # tests uncahnged
    for i, e in DATA:
        yield func, i, i

def test_zen_to_han():
    def func(input, expected):
        output = kana.to_han(input)
        assert output, "%r expected, got %r" % (expected, output)

    for e, i in DATA:
        yield func, i, e

    # tests uncahnged
    for i, e in DATA:
        yield func, e, e
