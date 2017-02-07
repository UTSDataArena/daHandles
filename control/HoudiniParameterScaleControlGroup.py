from euclid import *
from omega import *


from daHandles.control.ScaleControlGroup import Scale, ScaleControlGroup
from daHandles.control.utility.Axis import Axis
from daHandles.control.utility.Direction import Direction


class HoudiniParameterScaleControlGroup(ScaleControlGroup):

    def __init__(self, parent, builder, bounding_box, ui_context, parameter_mapping):

        self.parameter_mapping = parameter_mapping

        self.min_value = None
        self.max_value = None

        super(HoudiniParameterScaleControlGroup, self).__init__(parent, builder, bounding_box, ui_context)

    def build_control(self, id):
        return self.builder.set_id(id).set_parent(self).set_ui_context(self.ui_context).set_parameter(self.parameter_mapping[id]).build()

    def set_min_value(self, min_value):
        self.min_value = min_value

    def set_max_value(self, max_value):
        self.max_value = max_value

    def on_manipulate(self, control, origin, movement):

        axis = self.get_control_axis(control)
        direction = Direction.get_direction(axis, origin, movement)
        value = control.parameter.get_value(control.value_index) + (Scale.INCREMENT * direction)

        if (not self.min_value or self.min_value <= value) and (not self.max_value or value <= self.max_value):

            if axis == Axis.X_AXIS:
                control.get_geo().translate(Vector3(control.increment * direction, 0, 0), Space.Parent)
            elif axis == Axis.Y_AXIS:
                control.get_geo().translate(Vector3(0, control.increment * direction, 0), Space.Parent)
            elif axis == Axis.Z_AXIS:
                control.get_geo().translate(Vector3(0, 0, control.increment * direction), Space.Parent)

            control.parameter.set_value(value, control.value_index)
