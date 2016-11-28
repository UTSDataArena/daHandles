from euclid import *
from omega import *

from pyhandles.control.TriAxisControlGroup import TriAxisControlGroup


class Translation(object):

    POSITIVE = 1
    NEGATIVE = -1

    INCREMENT = 0.1

    @staticmethod
    def translate(axis, origin, delta):

        translation = Vector3(0, 0, 0)

        if axis == TriAxisControlGroup.X_AXIS:
            direction = Translation.NEGATIVE if delta.x <= origin.x else Translation.POSITIVE
            translation.x += Translation.INCREMENT * direction

        elif axis == TriAxisControlGroup.Y_AXIS:
            direction = Translation.POSITIVE if delta.y <= origin.y else Translation.NEGATIVE
            translation.y += Translation.INCREMENT * direction

        elif axis == TriAxisControlGroup.Z_AXIS:
            direction = Translation.POSITIVE if delta.x <= origin.x else Translation.NEGATIVE
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
