# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - 2023 -- Lars Heuer
# All rights reserved.
#
# License: BSD License
#
"""\
XBM related tests.
"""
from __future__ import unicode_literals, absolute_import
import io
import re
import pytest
import segno


def _decompose_xbm(s):
    # Inspired by test case PyQRCode (c) Michael Nooner, BSD License
    # See <https://github.com/mnooner256/pyqrcode/blob/master/tests/test_xbm.py>
    width = re.search(r'width ([0-9]+)', s).group(1)
    height = re.search(r'height ([0-9]+)', s).group(1)
    bits = re.findall(r'(0x[0-9][0-9])', s)
    return int(width), int(height), bits


def test_defaults():
    qr = segno.make_qr('test')
    out = io.StringIO()
    qr.save(out, kind='xbm')
    width, height = qr.symbol_size()
    assert '#define img_width {0}'.format(width) in out.getvalue()
    assert '#define img_height {0}'.format(height) in out.getvalue()
    assert 'static unsigned char img_bits[] = {' in out.getvalue()


def test_name():
    qr = segno.make_qr('test')
    out = io.StringIO()
    qr.save(out, kind='xbm', name='bla_bla')
    width, height = qr.symbol_size()
    assert '#define bla_bla_width {0}'.format(width) in out.getvalue()
    assert '#define bla_bla_height {0}'.format(height) in out.getvalue()
    assert 'static unsigned char bla_bla_bits[] = {' in out.getvalue()


def test_scale():
    expected = '''#define test_width 116
#define test_height 116
static unsigned char test_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x0f, 0x00, 0xff, 0xff, 0xff,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x0f, 0x00,
   0xff, 0xff, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x0f,
   0x00, 0x0f, 0x00, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0xff,
   0xff, 0xff, 0x0f, 0x00, 0x0f, 0x00, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0xf0, 0xff, 0x0f, 0x0f, 0x00, 0x00,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0xf0, 0xff, 0x0f,
   0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f,
   0xf0, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0x00, 0x00, 0x0f, 0xf0, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x0f, 0x0f, 0x00, 0x0f, 0xff, 0x0f,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x0f, 0x0f, 0x00,
   0x0f, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f,
   0x0f, 0x0f, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0xff, 0x0f, 0x0f, 0x0f, 0x0f, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0xff, 0x0f,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f,
   0x0f, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f,
   0x0f, 0x0f, 0x0f, 0x0f, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0xff, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0xff, 0x0f, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0xf0, 0xf0, 0x00, 0x0f, 0xff, 0x0f,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0xf0, 0xf0, 0x00,
   0x0f, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f,
   0xf0, 0xf0, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0xff, 0x0f, 0x0f, 0xf0, 0xf0, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0xf0, 0xf0, 0x00, 0x0f, 0x00, 0x00,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0xf0, 0xf0, 0x00,
   0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f,
   0xf0, 0xf0, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0x00, 0x00, 0x0f, 0xf0, 0xf0, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0xff, 0xff, 0xff, 0x0f, 0x0f, 0x0f, 0x0f, 0xff, 0xff, 0xff,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x0f, 0x0f, 0x0f, 0x0f,
   0xff, 0xff, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x0f,
   0x0f, 0x0f, 0x0f, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0xff,
   0xff, 0xff, 0x0f, 0x0f, 0x0f, 0x0f, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0xf0, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0xf0, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0xf0, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0xf0, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0xf0, 0x0f, 0xff, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x0f,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0x0f, 0xff, 0x00, 0xf0, 0x00,
   0x00, 0xf0, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0x0f, 0xff,
   0x00, 0xf0, 0x00, 0x00, 0xf0, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0xf0, 0x0f, 0xff, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x0f, 0x00, 0x00, 0x00,
   0x00, 0x00, 0xff, 0xff, 0x00, 0xf0, 0x0f, 0x0f, 0xf0, 0xf0, 0xff, 0x0f,
   0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0x00, 0xf0, 0x0f, 0x0f, 0xf0,
   0xf0, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0x00, 0xf0,
   0x0f, 0x0f, 0xf0, 0xf0, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
   0xff, 0x00, 0xf0, 0x0f, 0x0f, 0xf0, 0xf0, 0xff, 0x0f, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0x0f, 0xf0, 0xff, 0x00, 0x00, 0x0f, 0xf0, 0x00, 0xff,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x0f, 0xf0, 0xff, 0x00, 0x00, 0x0f,
   0xf0, 0x00, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x0f, 0xf0, 0xff,
   0x00, 0x00, 0x0f, 0xf0, 0x00, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0x0f, 0xf0, 0xff, 0x00, 0x00, 0x0f, 0xf0, 0x00, 0xff, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0xf0, 0x0f, 0x00, 0x00, 0x00, 0xf0, 0xf0, 0xff, 0x0f, 0x0f,
   0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0x0f, 0x00, 0x00, 0x00, 0xf0, 0xf0,
   0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0x0f, 0x00, 0x00,
   0x00, 0xf0, 0xf0, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0,
   0x0f, 0x00, 0x00, 0x00, 0xf0, 0xf0, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0xf0, 0xf0, 0x0f, 0x0f, 0x00, 0xf0, 0xf0, 0x0f, 0x00,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0xf0, 0x0f, 0x0f, 0x00, 0xf0,
   0xf0, 0x0f, 0x00, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0xf0, 0x0f,
   0x0f, 0x00, 0xf0, 0xf0, 0x0f, 0x00, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00,
   0xf0, 0xf0, 0x0f, 0x0f, 0x00, 0xf0, 0xf0, 0x0f, 0x00, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x0f, 0x00, 0x0f, 0x00, 0x0f,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x0f, 0x00,
   0x0f, 0x00, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0xff, 0x0f, 0x00, 0x0f, 0x00, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0xff, 0x0f, 0x00, 0x0f, 0x00, 0x0f, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xf0, 0xff, 0x00, 0xf0, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xf0, 0xff,
   0x00, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x0f,
   0xff, 0xf0, 0xff, 0x00, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
   0xff, 0xff, 0x0f, 0xff, 0xf0, 0xff, 0x00, 0xf0, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0xf0, 0x00, 0x00, 0x00, 0xf0, 0x0f,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0xf0, 0x00, 0x00,
   0x00, 0xf0, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f,
   0xf0, 0x00, 0x00, 0x00, 0xf0, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0x00, 0x00, 0x0f, 0xf0, 0x00, 0x00, 0x00, 0xf0, 0x0f, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0xff, 0xf0, 0xff, 0x0f, 0x0f, 0xf0,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0xff, 0xf0, 0xff,
   0x0f, 0x0f, 0xf0, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f,
   0xff, 0xf0, 0xff, 0x0f, 0x0f, 0xf0, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0xff, 0x0f, 0x0f, 0xff, 0xf0, 0xff, 0x0f, 0x0f, 0xf0, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0xff, 0x0f, 0xf0, 0x0f, 0x0f, 0x0f,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0xff, 0x0f, 0xf0,
   0x0f, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f,
   0xff, 0x0f, 0xf0, 0x0f, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0xff, 0x0f, 0x0f, 0xff, 0x0f, 0xf0, 0x0f, 0x0f, 0x0f, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x00, 0xf0, 0x0f, 0xf0, 0xff, 0xff,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f, 0x00, 0xf0, 0x0f,
   0xf0, 0xff, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0x0f, 0x0f,
   0x00, 0xf0, 0x0f, 0xf0, 0xff, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0xff, 0x0f, 0x0f, 0x00, 0xf0, 0x0f, 0xf0, 0xff, 0xff, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x0f, 0x00, 0xff,
   0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f,
   0x0f, 0x00, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f,
   0x00, 0x00, 0x0f, 0x0f, 0x00, 0xff, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x0f,
   0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x0f, 0x00, 0xff, 0x0f, 0x00, 0x00,
   0x00, 0x00, 0xff, 0xff, 0xff, 0x0f, 0xf0, 0xff, 0xf0, 0xff, 0x0f, 0x0f,
   0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x0f, 0xf0, 0xff, 0xf0,
   0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x0f,
   0xf0, 0xff, 0xf0, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
   0xff, 0xff, 0x0f, 0xf0, 0xff, 0xf0, 0xff, 0x0f, 0x0f, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
'''
    scale = 4
    qr = segno.make('Test', error='H')
    out = io.StringIO()
    qr.save(out, kind='xbm', scale=scale)
    res = out.getvalue()
    width, height = qr.symbol_size(scale=scale)
    expected_width, expected_height, expected_bits = _decompose_xbm(expected)
    out_width, out_height, out_bits = _decompose_xbm(res)
    assert expected_width == width
    assert expected_height == height
    assert expected_width == out_width
    assert expected_height == out_height
    assert len(expected_bits) == len(out_bits)
    assert expected_bits == out_bits


if __name__ == '__main__':
    pytest.main([__file__])
