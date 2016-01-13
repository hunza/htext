# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import six

BASIC_LATIN_RE = re.compile(r'[\u0021-\u007E]')
WHITESPACE_RE = re.compile("[\s]+", re.UNICODE)


def force_text(value):
    if isinstance(value, six.text_type):
        return value
    elif isinstance(value, six.string_types):
        return six.b(value).decode('utf-8')
    else:
        value = str(value)
        return value if isinstance(value, six.text_type) else value.decode('utf-8')


def basic_latin_to_fullwidth(value):
    """
    基本ラテン文字を全角に変換する
    U+0021..U+007FはU+FF01..U+FF5Eに対応しているので
    コードポイントに差分の0xFEE0を足す
    """
    _value = value.replace(' ', '\u3000')
    return BASIC_LATIN_RE.sub(lambda x: unichr(ord(x.group(0)) + 0xFEE0), _value)


def aggregate_whitespace(value):
    return ' '.join(WHITESPACE_RE.split(value))
