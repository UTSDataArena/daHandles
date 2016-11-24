import math

from cyclops import *
from euclid import *
from omega import *

from pyhandles.control.ControlGroup import ControlGroup


class RotateControlGroup(ControlGroup):

    DELTA = 0.5

    def __init__(self, parent, builder, ui_context):
        super(RotateControlGroup, self).__init__(parent, ui_context)

        self.id = '%s.rotate' % parent.get_id()

        self.x_axis_control = builder.set_id('x').set_parent(self).set_ui_context(ui_context).build()
        self.y_axis_control = builder.set_id('y').set_parent(self).set_ui_context(ui_context).build()
        self.z_axis_control = builder.set_id('z').set_parent(self).set_ui_context(ui_context).build()

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

        axis = None
        rotation = 0

        if control == self.x_axis_control:
            axis = Vector3(1, 0, 0)
            if movement.x <= origin.x:
                rotation += RotateControlGroup.DELTA
            else:
                rotation -= RotateControlGroup.DELTA

        elif control == self.y_axis_control:
            axis = Vector3(0, 1, 0)
            if movement.x <= origin.x:
                rotation -= RotateControlGroup.DELTA
            else:
                rotation += RotateControlGroup.DELTA

        elif control == self.z_axis_control:
            axis = Vector3(0, 0, 1)
            if movement.x <= origin.x:
                rotation += RotateControlGroup.DELTA
            else:
                rotation -= RotateControlGroup.DELTA

        self.parent.node.rotate(axis, math.radians(rotation), Space.Local)
