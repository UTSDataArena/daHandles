import unittest

from pyhandles.control.Control import Control
from pyhandles.control.ControlGroup import ControlGroup


class ControlGroupTestCase(unittest.TestCase):

    class MockContext(object):
        pass

    class MockParent(object):
        pass

    class MockControl(Control):

        def __init__(self):
            super(Control, self).__init__()

            self.visible = False
            self.released = False

        def build(self):
            super(ControlGroupTestCase.MockControl, self).build()

        def get_geo(self):
            return 'geo'

        def set_visible(self, visible):
            self.visible = visible

        def match(self, candidate):
            return [self]

        def on_release(self, context):
            super(ControlGroupTestCase.MockControl, self).on_release(context)
            self.released = True

    def setUp(self):
        self.parent = ControlGroupTestCase.MockParent()
        self.control_group = ControlGroup(self.parent, ControlGroupTestCase.MockContext())

    def testConstruct(self):
        self.assertEqual(self.parent, self.control_group.parent)
        self.assertEqual(0, len(self.control_group.controls))

    def testBuild(self):
        with self.assertRaises(NotImplementedError):
            self.control_group.build()

    def testGetGeo_noControls(self):
        self.assertEquals([], self.control_group.get_geo())

    def testGetGeo_withControls(self):
        control = ControlGroupTestCase.MockControl()
        self.control_group.controls.append(control)

        geo = self.control_group.get_geo()

        self.assertEquals(1, len(geo))
        self.assertTrue('geo' in geo)

    def testMatch_noControls(self):
        self.assertEquals([], self.control_group.match(None))

    def testMatch_withControls(self):
        control = ControlGroupTestCase.MockControl()
        self.control_group.controls.append(control)

        match = self.control_group.match(control)

        self.assertEquals(2, len(match))
        self.assertTrue(control in match)
        self.assertTrue(self.control_group in match)

    def testPrepare_noControls(self):
        try:
            self.control_group.prepare(None, [])
        except:
            self.fail('Unexpected exception encountered!')

    def testPrepare_unselectedControl(self):
        control = ControlGroupTestCase.MockControl()
        self.control_group.controls.append(control)

        self.control_group.prepare(None, [])

        self.assertFalse(control.released)

    def testPrepare_selectedMatchingControl(self):
        control = ControlGroupTestCase.MockControl()
        self.control_group.controls.append(control)

        control.is_selected = True

        self.control_group.prepare(control, [])

        self.assertFalse(control.released)

    def testPrepare_selectedNonMatchingControl(self):
        c1 = ControlGroupTestCase.MockControl()
        c2 = ControlGroupTestCase.MockControl()

        c1.is_selected = True

        self.control_group.controls.append(c1)
        self.control_group.prepare(c2, [])

        self.assertTrue(c1.released)
        self.assertFalse(c2.released)

    def testOnSelect_noControls(self):
        with self.assertRaises(IndexError):
            self.control_group.on_select([])

    def testOnSelect_unselectedControl(self):
        control = ControlGroupTestCase.MockControl()
        self.control_group.controls.append(control)

        self.control_group.on_select([control])

        self.assertTrue(self.control_group.is_selected)
        self.assertTrue(control.is_selected)
        self.assertFalse(control.released)

    def testOnSelect_selectedMatchingControl(self):
        control = ControlGroupTestCase.MockControl()
        self.control_group.controls.append(control)

        control.is_selected = True
        self.control_group.is_selected = True

        self.control_group.on_select([control])

        self.assertTrue(self.control_group.is_selected)
        self.assertTrue(control.is_selected)
        self.assertFalse(control.released)

    def testOnSelect_selectedNonMatchingControl(self):
        c1 = ControlGroupTestCase.MockControl()
        c2 = ControlGroupTestCase.MockControl()

        c1.is_selected = True
        self.control_group.is_selected = True

        self.control_group.controls.append(c1)
        self.control_group.controls.append(c2)

        self.control_group.on_select([c2])

        self.assertNotEqual(c1, c2)

        self.assertTrue(c1.released)
        self.assertFalse(c2.released)
        self.assertFalse(c1.is_selected)
        self.assertTrue(c2.is_selected)
        self.assertTrue(self.control_group.is_selected)

    def testOnRelease_noControls(self):
        with self.assertRaises(IndexError):
            self.control_group.on_release([])

    def testOnRelease_unselectedControl(self):
        control = ControlGroupTestCase.MockControl()
        self.control_group.controls.append(control)

        self.control_group.on_release([control])

        self.assertFalse(self.control_group.is_selected)
        self.assertFalse(control.is_selected)
        self.assertTrue(control.released)

    def testOnRelease_selectedMatchingControl(self):
        control = ControlGroupTestCase.MockControl()
        self.control_group.controls.append(control)

        control.is_selected = True
        self.control_group.is_selected = True

        self.control_group.on_release([control])

        self.assertFalse(self.control_group.is_selected)
        self.assertFalse(control.is_selected)
        self.assertTrue(control.released)

    def testOnRelease_selectedNonMatchingControl(self):
        c1 = ControlGroupTestCase.MockControl()
        c2 = ControlGroupTestCase.MockControl()

        c1.is_selected = True
        self.control_group.is_selected = True

        self.control_group.controls.append(c1)
        self.control_group.controls.append(c2)

        self.control_group.on_release([c2])

        self.assertNotEqual(c1, c2)

        self.assertTrue(c1.released)
        self.assertTrue(c2.released)
        self.assertFalse(c1.is_selected)
        self.assertFalse(c2.is_selected)
        self.assertFalse(self.control_group.is_selected)

    def testOnManipulate(self):
        with self.assertRaises(NotImplementedError):
            self.control_group.on_manipulate(None, None, None)
