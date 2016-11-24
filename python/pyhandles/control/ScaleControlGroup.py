import math

from cyclops import *
from euclid import *
from omega import *

from pyhandles.control.ControlGroup import ControlGroup


class ScaleControlGroup(ControlGroup):

    DELTA = 0.1

    def __init__(self, parent, builder, ui_context):
        super(ScaleControlGroup, self).__init__(parent, ui_context)

        self.id = '%s.scale' % parent.get_id()

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

        # our current strategy to ensure that controls do not get obscured by the
        # rescaled geometry is to also adjust the scale of the control so that it
        # remains visible - a better long term strategy would be to determine the
        # bounds of the geometry and draw the controls on the surface of this volume

        object_scale = self.parent.geo.getScale()
        handle_scale = control.get_geo().getScale()

        if control == self.x_axis_control:
            if movement.x <= origin.x:
                object_scale.x -= ScaleControlGroup.DELTA
                handle_scale.z -= ScaleControlGroup.DELTA * 0.5
            else:
                object_scale.x += ScaleControlGroup.DELTA
                handle_scale.z += ScaleControlGroup.DELTA * 0.5

        elif control == self.y_axis_control:
            if movement.y <= origin.y:
                object_scale.y += ScaleControlGroup.DELTA
                handle_scale.z += ScaleControlGroup.DELTA * 0.5
            else:
                object_scale.y -= ScaleControlGroup.DELTA
                handle_scale.z -= ScaleControlGroup.DELTA * 0.5

        elif control == self.z_axis_control:
            if movement.x <= origin.x:
                object_scale.z += ScaleControlGroup.DELTA
                handle_scale.z += ScaleControlGroup.DELTA * 0.5
            else:
                object_scale.z -= ScaleControlGroup.DELTA
                handle_scale.z -= ScaleControlGroup.DELTA * 0.5

        self.parent.geo.setScale(object_scale)
        control.get_geo().setScale(handle_scale)
