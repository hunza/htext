# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six


def force_text(value):
    if isinstance(value, six.text_type):
        return value
    elif isinstance(value, six.string_types):
        return six.b(value).decode()
    else:
        value = str(value)
        return value if isinstance(value, six.text_type) else value.decode()

