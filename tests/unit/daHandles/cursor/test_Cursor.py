import unittest

from daHandles.cursor.Cursor import Cursor


class CursorTestCase(unittest.TestCase):

    def setUp(self):
        self.cursor = Cursor('id')

    def testConstruct(self):
        self.assertEqual('id', self.cursor.id)

    def testOnEvent(self):
        with self.assertRaises(NotImplementedError):
            self.cursor.on_event()
