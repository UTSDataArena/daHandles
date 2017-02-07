from euclid import *
from omega import *

from daHandles.control.TriAxisControlGroup import TriAxisControlGroup
from daHandles.control.utility.Axis import Axis
from daHandles.control.utility.Direction import Direction


class Translation(object):

    INCREMENT = 0.1

    @staticmethod
    def translate(axis, origin, movement):

        translation = Vector3(0, 0, 0)
        direction = Direction.get_direction(axis, origin, movement)

        if axis == Axis.X_AXIS:
            translation.x += Translation.INCREMENT * direction
        elif axis == Axis.Y_AXIS:
            translation.y += Translation.INCREMENT * direction
        elif axis == Axis.Z_AXIS:
            translation.z += Translation.INCREMENT * direction

        return translation


class TranslateControlGroup(TriAxisControlGroup):

    def __init__(self, parent, builder, bounding_box, ui_context):
        super(TranslateControlGroup, self).__init__(parent, builder, bounding_box, ui_context)

        self.id = '%s.translate' % parent.get_id()

        self.build()
        self.set_visible(False)

    def on_manipulate(self, control, origin, movement):
        self.parent.node.translate(Translation.translate(self.get_control_axis(control), origin, movement), Space.Local)
