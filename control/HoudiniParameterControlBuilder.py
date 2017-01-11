from daHandles.control.ControlBuilder import ControlBuilder
from daHandles.control.HoudiniParameterControl import HoudiniParameterControl


class HoudiniParameterControlBuilder(ControlBuilder):

    def __init__(self):
        super(HoudiniParameterControlBuilder, self).__init__()

        self.geometry_builder = None
        self.control_parameter = None
        self.control_increment = 1

    def set_geometry_builder(self, geometry_builder):
        self.geometry_builder = geometry_builder
        return self

    def set_control_parameter(self, control_parameter):
        self.control_parameter = control_parameter
        return self

    def set_control_increment(self, control_increment):
        self.control_increment = control_increment
        return self

    def build(self):
        control = HoudiniParameterControl(self.id, self.parent, self.geometry_builder, self.ui_context)
        control.set_parameter(self.control_parameter)
        control.set_increment(self.control_increment)

        return control
