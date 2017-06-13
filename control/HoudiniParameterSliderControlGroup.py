from daHandles.control.ControlGroup import ControlGroup
from daHandles.control.utility.Direction import Direction


class HoudiniParameterSliderControlGroup(ControlGroup):

    def __init__(self, parent, builder, ui_context):
        super(HoudiniParameterSliderControlGroup, self).__init__(parent, ui_context)

        self.id = None
        self.axis = None
        self.control = None
        self.builder = builder

        self.build()
        self.set_visible(False)

    def build(self):

        self.control = self.builder.set_id('control').set_parent(self).set_ui_context(self.ui_context).build()
        self.control.set_effect('colored -d red')

        self.controls.append(self.control)

    def get_id(self):
        return self.id

    def get_axis(self):
        return self.axis

    def set_axis(self, axis):
        self.axis = axis

    def on_manipulate(self, control, origin, movement):

        direction = Direction.get_direction(self.axis, origin, movement)
        value = control.parameter.get_value(control.value_index) + (control.increment * direction)

        control.parameter.set_value(value, control.value_index)
