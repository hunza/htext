# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from htext.ja import regex

def test_hiragana():
    res = regex.hiragana.findall("カラマーゾフのきょうだい")
    assert res[0] == ("のきょうだい"), res

def test_hiranaga_mixed():
    res = regex.hiragana.findall("つみ と 罰")
    assert tuple(res) == ("つみ", "と"), res

def test_katakana():
    res = regex.katakana.findall("ドストヱフスキー")
    assert res[0] == ("ドストヱフスキー"), res

    res = regex.katakana.findall("ﾄﾞストｴﾌｽｷｰ")
    assert res[0] == "ﾄﾞストｴﾌｽｷｰ"

def test_katakana_mixed():
    res = regex.katakana.findall("カラマーゾフの兄弟")
    assert res[0] == ("カラマーゾフ"), res

def test_katakana_two_word():
    res = regex.katakana.findall("イワン・カラマーゾフ")
    assert tuple(res) == ("イワン", "カラマーゾフ"), res

def test_han_katakana():
    res = regex.katakana.findall("人はﾊﾟﾝのみにて生くるものにあらず")
    assert res[0] == "ﾊﾟﾝ"


