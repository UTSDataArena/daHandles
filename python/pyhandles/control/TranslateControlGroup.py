from euclid import *
from omega import *

from pyhandles.control.TriAxisControlGroup import TriAxisControlGroup


class Translation(object):

    INCREMENT = 0.1

    @staticmethod
    def translate(axis, origin, delta):

        translation = Vector3(0, 0, 0)

        if axis == TriAxisControlGroup.X_AXIS:
            if delta.x <= origin.x:
                translation.x -= Translation.INCREMENT
            else:
                translation.x += Translation.INCREMENT

        elif axis == TriAxisControlGroup.Y_AXIS:
            if delta.y <= origin.y:
                translation.y += Translation.INCREMENT
            else:
                translation.y -= Translation.INCREMENT

        elif axis == TriAxisControlGroup.Z_AXIS:
            if delta.x <= origin.x:
                translation.z += Translation.INCREMENT
            else:
                translation.z -= Translation.INCREMENT

        return translation


class TranslateControlGroup(TriAxisControlGroup):

    def __init__(self, parent, builder, ui_context):
        super(TranslateControlGroup, self).__init__(parent, builder, ui_context)

        self.id = '%s.translate' % parent.get_id()

        self.build()
        self.set_visible(False)

    def on_manipulate(self, control, origin, movement):
        self.parent.node.translate(Translation.translate(self.get_control_axis(control), origin, movement), Space.Local)
