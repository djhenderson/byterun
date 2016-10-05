"""Simple type tests for Byterun."""

from __future__ import print_function
import sys
from . import vmtest

import six

PY3, PY2 = six.PY3, not six.PY3

class TestSimpleTypes(vmtest.VmTestCase):

    def test_None(self):
        self.assert_ok("""
            n = None
            print(type(n), n)
            """)

    def test_bool(self):
        self.assert_ok("""
            t = True
            print(type(t), t)
            """)

    if PY3:
        def test_elipsis(self):
            self.assert_ok("""
                t = ...
                print(type(t), t)
                """)

    def test_NotImplemented(self):
        self.assert_ok("""
            t = NotImplemented
            print(type(t), t)
            """)

    def test_type(self):
        self.assert_ok("""
            t = type
            print(type(t), t)
            """)

    def test_int(self):
        self.assert_ok("""\
            i = 1
            print(type(i), i)
            """)

    if sys.version_info[:2] not in ((3, 3), (3, 4), (3, 5),):
        def test_long(self):
            self.assert_ok("""
                l = 4294967297L
                print(type(l), l)
                """)

    def test_float(self):
        self.assert_ok("""
            f = 3.1415926
            print(type(f), f)
            """)

    def test_complex(self):
        self.assert_ok("""
            c = (3.14-3.14j)
            print(type(c), c)
            """)

    def test_strt(self):
        self.assert_ok("""
            s = '''abc
                def'''
            print(type(s), s)
            """)

    def test_str(self):
        self.assert_ok("""
            s = 'abc'
            print(type(s), s)
            """)

    def test_rstr(self):
        self.assert_ok(r"""
            s = r'a\bc'
            print(type(s), s)
            """)

    def test_ustr(self):
        self.assert_ok("""
            s = u'abc'
            print(type(s), s)
            """)

    if sys.version_info[:2] not in ((3, 3), (3, 4), (3, 5),):
        def test_urstr(self):
            self.assert_ok(r"""
                s = ur'a\bc'
                print(type(s), s)
                """)

    def test_bytes(self):
        self.assert_ok("""
            s = bytes(range(1, 4))
            print(type(s), s)
            """)

    def test_bytes(self):
        self.assert_ok("""
            s = bytearray(b'abc')
            print(type(s), s)
            """)

    def test_bytearray(self):
        self.assert_ok("""
            s = bytearray(b'abc')
            print(type(s), s)
            """)

    def test_brstr(self):
        self.assert_ok(r"""
            s = br'a\bc'
            print(type(s), s)
            """)

    def test_tuple(self):
        self.assert_ok("""
            s = (1, 2, 3, 4)
            print(type(s), s)
            """)

    def test_list(self):
        self.assert_ok("""
            s = [1, 2, 3, 4]
            print(type(s), s)
            """)

    def test_set(self):
        self.assert_ok("""
            s = {1, 2, 3, 4}
            print(type(s), s)
            """)

    def test_dict(self):
        self.assert_ok("""
            s = {1: 'a', 2: 'b', 3: 'c', 4: 'd',}
            print(type(s), s)
            """)

    if PY2:
        def test_xrange(self):
            self.assert_ok("""
                r = xrange(1, 10, 2)
                print(type(r), r)
                """)

    if PY3:
        def test_range(self):
            self.assert_ok("""
                r = range(1, 10, 2)
                print(type(r), r)
                """)

    def test_object(self):
        self.assert_ok("""
            o = object
            print(type(o), o)
            """)

    def test_module(self):
        self.assert_ok("""
            import sys
            m = sys.modules['sys']
            print(type(m), m)
            """)

    # TODO: file-objects
    # TODO: callables
    # TODO: frozenset
