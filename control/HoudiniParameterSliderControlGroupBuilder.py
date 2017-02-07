from daHandles.control.ControlBuilder import ControlBuilder
from daHandles.control.HoudiniParameterSliderControlGroup import HoudiniParameterSliderControlGroup


class HoudiniParameterSliderControlGroupBuilder(ControlBuilder):

    def __init__(self):
        super(HoudiniParameterSliderControlGroupBuilder, self).__init__()

        self.control_builder = None
        self.axis = None

    def set_control_builder(self, control_builder):
        self.control_builder = control_builder
        return self

    def set_axis(self, axis):
        self.axis = axis
        return self

    def build(self):
        control = HoudiniParameterSliderControlGroup(self.parent, self.control_builder, self.ui_context)
        control.set_axis(self.axis)

        return control
