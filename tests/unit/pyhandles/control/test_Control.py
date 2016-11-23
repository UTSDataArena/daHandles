import unittest

from pyhandles.control.Control import Control


class ControlTestCase(unittest.TestCase):

    class MockContext(object):
        pass

    class MockParent(object):
        pass

    def setUp(self):
        self.parent = ControlTestCase.MockParent()
        self.control = Control(self.parent, ControlTestCase.MockContext())

    def testConstruct(self):
        self.assertEqual(self.parent, self.control.parent)

    def testBuild(self):
        with self.assertRaises(NotImplementedError):
            self.control.build()

    def testGetId(self):
        with self.assertRaises(NotImplementedError):
            self.control.get_id()

    def testGetGeo(self):
        with self.assertRaises(NotImplementedError):
            self.control.get_geo()

    def testSetVisible(self):
        with self.assertRaises(NotImplementedError):
            self.control.set_visible(True)

    def testSetMatch(self):
        with self.assertRaises(NotImplementedError):
            self.control.match(None)

    def testOnSelect(self):
        self.assertFalse(self.control.is_selected)
        self.control.on_select(None)
        self.assertTrue(self.control.is_selected)

    def testOnRelease(self):
        self.assertFalse(self.control.is_selected)
        self.control.on_release(None)
        self.assertFalse(self.control.is_selected)
