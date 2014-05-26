# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from htext.ja import chars

DATA = [
    ("コーリャ", "ｺｰﾘｬ"),
    ("ペレズヴォン", "ﾍﾟﾚｽﾞｳﾞｫﾝ"),
    ("アレクセイ・カラマーゾフ", "ｱﾚｸｾｲ･ｶﾗﾏｰｿﾞﾌ"),
    ("「スコトプリゴニエフスク」", "｢ｽｺﾄﾌﾟﾘｺﾞﾆｴﾌｽｸ｣"),
    ("。", "｡"),
    ("Ｕ２", "U2"),
    ]

def test_han_to_zen():
    def func(input, expected):
        output = chars.to_zen(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for zen, han in DATA:
        yield func, han, zen

    # tests uncahnged
    for zen, han in DATA:
        yield func, zen, zen

def test_zen_to_han():
    def func(input, expected):
        output = chars.to_han(input)
        assert output == expected, "%s expected, got %s" % (expected, output)

    for zen, han in DATA:
        yield func, zen, han

    # tests uncahnged
    for zen, han in DATA:
        yield func, han, han
