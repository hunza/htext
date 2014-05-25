# -*- coding: utf-8 -*-
from htext.ja.romanize.passport import romanize, reverse

NAMES = [(u'なんば', 'NAMBA'),
         (u'ほんま', 'HOMMA'),
         (u'さんぺい', 'SAMPEI'),
         (u'はっとり', 'HATTORI'),
         (u'きっかわ', 'KIKKAWA'),
         (u'ほっち', 'HOTCHI'),
         (u'ひゅうが', 'HYUGA'),
         (u'ちゅうま', 'CHUMA'),
         (u'えっちゅう', 'ETCHU'),
         (u'チュウマ', 'CHUMA'),
         ]

def test_hepburn():
    def func(input, expected):
        value = romanize(input)
        assert value == expected, u'%s expected, got %s' % (expected, value)

    for i, e in NAMES + [(u'はっちょう', 'HATCHO'),
                         (u'こうの', 'KONO'),
                         (u'おおの', 'ONO'),
                         (u'おーの', 'ONO'),
                         ]:
        yield func, i, e

def test_hepburn_vowels():
    def func(input, expected):
        value = romanize(input, long_vowels_h=True)
        assert value == expected, u'%s expected, got %s' % (expected, value)

    for i, e in NAMES + [(u'はっちょう', 'HATCHOH'),
                         (u'こうの', 'KOHNO'),
                         (u'おおの', 'OHNO'),
                         (u'おーの', 'ONO'),
                         ]:
        yield func, i, e

def test_reverse():
    def func(input, expected):
        try:
            value = reverse(input)
            assert value == expected, u'%s expected, got %s' % (expected, value)
        except NotImplementedError:
            # TODO
            pass

    for e, i in NAMES:
        yield func, i, e

