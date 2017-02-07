from euclid import *

from daHandles.control.TriAxisControlGroup import TriAxisControlGroup
from daHandles.control.utility.Axis import Axis
from daHandles.control.utility.Direction import Direction


class Scale(object):

    INCREMENT = 0.1

    @staticmethod
    def scale(axis, origin, movement, increment=INCREMENT):

        scale = Vector3(0, 0, 0)
        direction = Direction.get_direction(axis, origin, movement)

        if axis == Axis.X_AXIS:
            scale.x += increment * direction

        elif axis == Axis.Y_AXIS:
            scale.y += increment * direction

        elif axis == Axis.Z_AXIS:
            scale.z += increment * direction

        return scale


class ScaleControlGroup(TriAxisControlGroup):

    def __init__(self, parent, builder, bounding_box, ui_context):
        super(ScaleControlGroup, self).__init__(parent, builder, bounding_box, ui_context)

        self.id = '%s.scale' % parent.get_id()

        self.build()
        self.set_visible(False)

    def on_manipulate(self, control, origin, movement):
        axis = self.get_control_axis(control)
        direction = Direction.get_direction(axis, origin, movement)

        self.parent.get_geo().setScale(self.parent.get_geo().getScale() + Scale.scale(axis, origin, movement))

        if axis == Axis.X_AXIS:
            control.get_geo().translate(Vector3(Scale.INCREMENT / 2 * direction, 0, 0), Space.Parent)
        elif axis == Axis.Y_AXIS:
            control.get_geo().translate(Vector3(0, Scale.INCREMENT / 2 * direction, 0), Space.Parent)
        elif axis == Axis.Z_AXIS:
            control.get_geo().translate(Vector3(0, 0, Scale.INCREMENT / 2 * direction), Space.Parent)
