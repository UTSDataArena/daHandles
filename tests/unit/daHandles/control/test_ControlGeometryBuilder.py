import unittest

from daHandles.control.ControlGeometryBuilder import ControlGeometryBuilder


class ControlGeometryBuilderTestCase(unittest.TestCase):

    def setUp(self):
        self.builder = ControlGeometryBuilder()

    def testBuild(self):
        with self.assertRaises(NotImplementedError):
            self.builder.build()
