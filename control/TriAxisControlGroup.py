import math

from cyclops import *
from euclid import *
from omega import *

from daHandles.control.ControlGroup import ControlGroup


class TriAxisControlGroup(ControlGroup):
    """
    Base class for tri-axis control groups; not intended to be directly instantiated.
    """

    X_AXIS = 'x'
    Y_AXIS = 'y'
    Z_AXIS = 'z'

    def __init__(self, parent, builder, bounding_box, ui_context):
        super(TriAxisControlGroup, self).__init__(parent, ui_context)

        self.id = None
        self.x_axis_control = None
        self.y_axis_control = None
        self.z_axis_control = None

        self.builder = builder
        self.bounding_box = bounding_box

    def build(self):

        # note: this control group assumes that the provided geometry is positioned
        #       at the origin and is oriented along the z-axis

        self.x_axis_control = self.build_control(TriAxisControlGroup.X_AXIS)
        self.x_axis_control.set_effect('colored -d red')
        self.x_axis_control.geo.translate(Vector3(self.bounding_box[1].x, 0, 0), Space.Local)
        self.x_axis_control.geo.rotate(Vector3(0, 1, 0), math.radians(90), Space.Parent)

        self.y_axis_control = self.build_control(TriAxisControlGroup.Y_AXIS)
        self.y_axis_control.set_effect('colored -d green')
        self.y_axis_control.geo.translate(Vector3(0, self.bounding_box[1].y, 0), Space.Local)
        self.y_axis_control.geo.rotate(Vector3(1, 0, 0), math.radians(-90), Space.Parent)

        self.z_axis_control = self.build_control(TriAxisControlGroup.Z_AXIS)
        self.z_axis_control.set_effect('colored -d blue')
        self.z_axis_control.geo.translate(Vector3(0, 0, self.bounding_box[1].z), Space.Local)

        for control in [self.x_axis_control, self.y_axis_control, self.z_axis_control]:
            self.controls.append(control)

    def build_control(self, id):
        return self.builder.set_id(id).set_parent(self).set_ui_context(self.ui_context).build()

    def get_id(self):
        return self.id

    def get_control_axis(self, control):
        if control == self.x_axis_control:
            return TriAxisControlGroup.X_AXIS
        elif control == self.y_axis_control:
            return TriAxisControlGroup.Y_AXIS
        elif control == self.z_axis_control:
            return TriAxisControlGroup.Z_AXIS

    def on_manipulate(self, control, origin, movement):
        super(TriAxisControlGroup, self).on_manipulate(control, origin, movement)
