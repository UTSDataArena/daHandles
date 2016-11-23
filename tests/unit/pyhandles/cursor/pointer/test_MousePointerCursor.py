import unittest

from pyhandles.cursor.pointer.MousePointerCursor import MousePointerCursor


class MousePointerCursorTestCase(unittest.TestCase):

    def setUp(self):

        self.cursor = MousePointerCursor('id')

    def testConstruct(self):

        self.assertEqual('id', self.cursor.id)

    def testOnEvent(self):

        try:
            self.cursor.on_event()
        except NotImplementedError:
            self.fail('Unexpected NotImplementError encountered!')
