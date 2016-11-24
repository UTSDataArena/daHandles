import math

from cyclops import *
from euclid import *
from omega import *

from pyhandles.control.ControlGroup import ControlGroup


class TranslateControlGroup(ControlGroup):

    DELTA = 0.1

    def __init__(self, parent, context, builder):
        super(TranslateControlGroup, self).__init__(parent, context)

        self.id = '%s.translate' % parent.get_id()

        self.x_axis_control = builder.set_id('x').set_parent(self).set_context(context).build()
        self.y_axis_control = builder.set_id('y').set_parent(self).set_context(context).build()
        self.z_axis_control = builder.set_id('z').set_parent(self).set_context(context).build()

        self.build()
        self.set_visible(False)

    def build(self):

        self.x_axis_control.set_effect('colored -d red')
        self.x_axis_control.geo.rotate(Vector3(0, 1, 0), math.radians(90), Space.Parent)

        self.y_axis_control.set_effect('colored -d green')
        self.y_axis_control.geo.rotate(Vector3(1, 0, 0), math.radians(-90), Space.Parent)

        self.z_axis_control.set_effect('colored -d blue')

        for control in [self.x_axis_control, self.y_axis_control, self.z_axis_control]:
            self.controls.append(control)
            setEventFunction(control.on_event)

    def get_id(self):
        return self.id

    def on_manipulate(self, control, origin, movement):

        translation = Vector3(0, 0, 0)

        if control == self.x_axis_control:
            if movement.x <= origin.x:
                translation.x -= TranslateControlGroup.DELTA
            else:
                translation.x += TranslateControlGroup.DELTA

        elif control == self.y_axis_control:
            if movement.y <= origin.y:
                translation.y += TranslateControlGroup.DELTA
            else:
                translation.y -= TranslateControlGroup.DELTA

        elif control == self.z_axis_control:
            if movement.x <= origin.x:
                translation.z += TranslateControlGroup.DELTA
            else:
                translation.z -= TranslateControlGroup.DELTA

        self.parent.node.translate(translation, Space.Local)
