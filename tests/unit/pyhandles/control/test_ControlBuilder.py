import unittest

from pyhandles.control.ControlBuilder import ControlBuilder


class ControlBuilderTestCase(unittest.TestCase):

    def setUp(self):
        self.builder = ControlBuilder()

    def testConstruct(self):
        self.assertIsNone(self.builder.id)
        self.assertIsNone(self.builder.parent)

    def testBuild(self):
        with self.assertRaises(NotImplementedError):
            self.builder.build()
