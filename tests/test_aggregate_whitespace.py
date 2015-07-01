# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from htext.ja.utils import aggregate_whitespace


def test_aggregate_whitespace():
    value = 'a  b\t\t\tc\n\n\nd \t\ne'
    result = aggregate_whitespace(value)
    expected = 'a b c d e'
    assert result == expected
