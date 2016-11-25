import math

from euclid import *
from omega import *

from pyhandles.control.TriAxisControlGroup import TriAxisControlGroup


class Rotation(object):

    INCREMENT = 1.0

    @staticmethod
    def rotate(axis, origin, delta):

        rotation = 0
        rotation_axis = None

        if axis == TriAxisControlGroup.X_AXIS:
            rotation_axis = Vector3(1, 0, 0)
            if delta.y <= origin.y:
                rotation += Rotation.INCREMENT
            else:
                rotation -= Rotation.INCREMENT

        elif axis == TriAxisControlGroup.Y_AXIS:
            rotation_axis = Vector3(0, 1, 0)
            if delta.x <= origin.x:
                rotation -= Rotation.INCREMENT
            else:
                rotation += Rotation.INCREMENT

        elif axis == TriAxisControlGroup.Z_AXIS:
            rotation_axis = Vector3(0, 0, 1)
            if delta.y <= origin.y:
                rotation += Rotation.INCREMENT
            else:
                rotation -= Rotation.INCREMENT

        return rotation_axis, math.radians(rotation)


class RotateControlGroup(TriAxisControlGroup):

    def __init__(self, parent, builder, ui_context):
        super(RotateControlGroup, self).__init__(parent, builder, ui_context)

        self.id = '%s.rotate' % parent.get_id()

        self.build()
        self.set_visible(False)

    def on_manipulate(self, control, origin, movement):
        axis, angle = Rotation.rotate(self.get_control_axis(control), origin, movement)
        self.parent.node.rotate(axis, angle, Space.Local)
