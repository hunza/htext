# -*- coding: utf-8 -*-
from textutil_ja.romanize.hepburn import romanize

def test_romanize():
    def func(input, expected):
        value = romanize(input)
        assert value == expected, u'%s expected, got %s' % (expected, value)

    for input, expected in ((u"つみ と ばつ", u"TSUMI TO BATSU"),
                            (u"カラマーゾフ の きょうだい", u"KARAMAAZOFU NO KYOUDAI"),
                            (u"ペレズヴォン", u"PEREZUVON"),
                            ):
        yield func, input, expected

