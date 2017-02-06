from euclid import *
from omega import *


from daHandles.control.TriAxisControlGroup import TriAxisControlGroup
from daHandles.control.utility.Direction import Direction


class Scale(object):

    INCREMENT = 0.1

    @staticmethod
    def scale(axis, origin, delta):

        scale = Vector3(0, 0, 0)

        if axis == TriAxisControlGroup.X_AXIS:
            direction = Direction.NEGATIVE if delta.x <= origin.x else Direction.POSITIVE
            scale.x += Scale.INCREMENT * direction

        elif axis == TriAxisControlGroup.Y_AXIS:
            direction = Direction.POSITIVE if delta.y <= origin.y else Direction.NEGATIVE
            scale.y += Scale.INCREMENT * direction

        elif axis == TriAxisControlGroup.Z_AXIS:
            direction = Direction.POSITIVE if delta.x <= origin.x else Direction.NEGATIVE
            scale.z += Scale.INCREMENT * direction

        return scale


class ScaleControlGroup(TriAxisControlGroup):

    def __init__(self, parent, builder, bounding_box, ui_context):
        super(ScaleControlGroup, self).__init__(parent, builder, bounding_box, ui_context)

        self.id = '%s.scale' % parent.get_id()

        self.build()
        self.set_visible(False)

    def on_manipulate(self, control, origin, movement):
        axis = self.get_control_axis(control)

        self.parent.get_geo().setScale(self.parent.get_geo().getScale() + Scale.scale(axis, origin, movement))

        if axis == TriAxisControlGroup.X_AXIS:
            direction = Direction.NEGATIVE if movement.x <= origin.x else Direction.POSITIVE
            control.get_geo().translate(Vector3(Scale.INCREMENT / 2 * direction, 0, 0), Space.Parent)
        elif axis == TriAxisControlGroup.Y_AXIS:
            direction = Direction.POSITIVE if movement.y <= origin.y else Direction.NEGATIVE
            control.get_geo().translate(Vector3(0, Scale.INCREMENT / 2 * direction, 0), Space.Parent)
        elif axis == TriAxisControlGroup.Z_AXIS:
            direction = Direction.POSITIVE if movement.x <= origin.x else Direction.NEGATIVE
            control.get_geo().translate(Vector3(0, 0, Scale.INCREMENT / 2 * direction), Space.Parent)
