# -*- coding: utf-8 -*-
from htext.ja import regex

def test_hiragana():
    res = regex.hiragana.findall(u"カラマーゾフのきょうだい")
    assert res[0] == (u"のきょうだい"), res

def test_hiranaga_mixed():
    res = regex.hiragana.findall(u"つみ と 罰")
    assert tuple(res) == (u"つみ", u"と"), res

def test_katakana():
    res = regex.katakana.findall(u"ドストヱフスキー")
    assert res[0] == (u"ドストヱフスキー"), res

    res = regex.katakana.findall(u"ﾄﾞストｴﾌｽｷｰ")
    assert res[0] == u"ﾄﾞストｴﾌｽｷｰ"

def test_katakana_mixed():
    res = regex.katakana.findall(u"カラマーゾフの兄弟")
    assert res[0] == (u"カラマーゾフ"), res

def test_katakana_two_word():
    res = regex.katakana.findall(u"イワン・カラマーゾフ")
    assert tuple(res) == (u"イワン", u"カラマーゾフ"), res

def test_han_katakana():
    res = regex.katakana.findall(u"人はﾊﾟﾝのみにて生くるものにあらず")
    assert res[0] == u"ﾊﾟﾝ"


