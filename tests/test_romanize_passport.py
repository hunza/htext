# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from htext.ja.romanize.passport import romanize, reverse

NAMES = [('なんば', 'NAMBA'),
         ('ほんま', 'HOMMA'),
         ('さんぺい', 'SAMPEI'),
         ('はっとり', 'HATTORI'),
         ('きっかわ', 'KIKKAWA'),
         ('ほっち', 'HOTCHI'),
         ('ひゅうが', 'HYUGA'),
         ('ちゅうま', 'CHUMA'),
         ('えっちゅう', 'ETCHU'),
         ('チュウマ', 'CHUMA'),
         ]

def test_hepburn():
    def func(input, expected):
        value = romanize(input)
        assert value == expected, '%s expected, got %s' % (expected, value)

    for i, e in NAMES + [('はっちょう', 'HATCHO'),
                         ('こうの', 'KONO'),
                         ('おおの', 'ONO'),
                         ('おーの', 'ONO'),
                         ]:
        yield func, i, e

def test_hepburn_vowels():
    def func(input, expected):
        value = romanize(input, long_vowels_h=True)
        assert value == expected, '%s expected, got %s' % (expected, value)

    for i, e in NAMES + [('はっちょう', 'HATCHOH'),
                         ('こうの', 'KOHNO'),
                         ('おおの', 'OHNO'),
                         ('おーの', 'ONO'),
                         ]:
        yield func, i, e

def test_reverse():
    def func(input, expected):
        try:
            value = reverse(input)
            assert value == expected, '%s expected, got %s' % (expected, value)
        except NotImplementedError:
            # TODO
            pass

    for e, i in NAMES:
        yield func, i, e

