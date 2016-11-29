import unittest

from daHandles.selection.Selectable import Selectable


class SelectableTestCase(unittest.TestCase):

    def setUp(self):
        self.selectable = Selectable()

    def testConstruct(self):
        self.assertFalse(self.selectable.is_selected)

    def testGetId(self):
        with self.assertRaises(NotImplementedError):
            self.selectable.get_id()

    def testMatch(self):
        with self.assertRaises(NotImplementedError):
            self.selectable.match(None)

    def testOnSelect(self):
        self.assertFalse(self.selectable.is_selected)
        self.selectable.on_select(None)
        self.assertTrue(self.selectable.is_selected)

    def testOnRelease(self):
        self.assertFalse(self.selectable.is_selected)
        self.selectable.on_release(None)
        self.assertFalse(self.selectable.is_selected)
