# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from htext.ja.utils import basic_latin_to_fullwidth


def test_basic_latin_to_fullwidth():
    value = ''.join(six.unichr(x) for x in range(0x20, 0x7F))
    result = basic_latin_to_fullwidth(value)
    expected = ''.join((
        '\u3000！\uFF02＃＄％＆\uFF07（）＊＋，－．／',
        '０１２３４５６７８９：；＜＝＞？',
        '＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯ',
        'ＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿',
        '｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏ',
        'ｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～'))
    assert result == expected
