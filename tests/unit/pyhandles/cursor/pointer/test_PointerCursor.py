import unittest

from pyhandles.cursor.pointer.PointerCursor import PointerCursor


class PointerCursorTestCase(unittest.TestCase):

    def setUp(self):

        self.cursor = PointerCursor('id')

    def testConstruct(self):

        self.assertEqual('id', self.cursor.id)

    def testOnEvent(self):

        try:
            self.cursor.on_event()
        except NotImplementedError:
            self.fail('Unexpected NotImplementError encountered!')
