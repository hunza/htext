# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from htext.ja.romanize.hepburn import romanize, reverse


def test_romanize():
    def func(input, expected):
        value = romanize(input)
        assert value == expected, '%s expected, got %s' % (expected, value)

    for input, expected in (("つみ と ばつ", "TSUMI TO BATSU"),
                            ("カラマーゾフ の きょうだい", "KARAMAAZOFU NO KYOUDAI"),
                            ("ペレズヴォン", "PEREZUVON"),
                            ):
        yield func, input, expected


def test_reverse():
    def func(input, expected):
        value = reverse(input)
        assert value == expected, '%s expected, got %s' % (expected, value)

    for input, expected in (("TSUMI TO BATSU", "つみ と ばつ"),
                            ("WOKKA", "をっか"),
                            ("shimpan", "しんぱん"),
                            ("shinpan", "しんぱん"),
                            ):
        yield func, input, expected
