import math

from euclid import *
from omega import *

from daHandles.control.TriAxisControlGroup import TriAxisControlGroup
from daHandles.control.utility.Axis import Axis
from daHandles.control.utility.Direction import Direction


class Rotation(object):

    INCREMENT = 1.0

    @staticmethod
    def rotate(axis, origin, delta):

        direction = None

        rotation = 0
        rotation_axis = None

        if axis == Axis.X_AXIS:
            rotation_axis = Vector3(1, 0, 0)
            direction = Direction.NEGATIVE if delta.y <= origin.y else Direction.POSITIVE

        elif axis == Axis.Y_AXIS:
            rotation_axis = Vector3(0, 1, 0)
            direction = Direction.NEGATIVE if delta.x <= origin.x else Direction.POSITIVE

        elif axis == Axis.Z_AXIS:
            rotation_axis = Vector3(0, 0, 1)
            direction = Direction.POSITIVE if delta.y <= origin.y else Direction.NEGATIVE

        rotation += Rotation.INCREMENT * direction

        return rotation_axis, math.radians(rotation)


class RotateControlGroup(TriAxisControlGroup):

    def __init__(self, parent, builder, bounding_box, ui_context):
        super(RotateControlGroup, self).__init__(parent, builder, bounding_box, ui_context)

        self.id = '%s.rotate' % parent.get_id()

        self.build()
        self.set_visible(False)

    def on_manipulate(self, control, origin, movement):
        axis, angle = Rotation.rotate(self.get_control_axis(control), origin, movement)
        self.parent.node.rotate(axis, angle, Space.Local)
