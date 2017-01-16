from daHandles.control.ControlBuilder import ControlBuilder
from daHandles.control.HoudiniParameterControl import HoudiniParameterControl


class HoudiniParameterControlBuilder(ControlBuilder):

    def __init__(self):
        super(HoudiniParameterControlBuilder, self).__init__()

        self.geometry_builder = None
        self.control_parameter = None
        self.control_value_index = 0
        self.control_increment = 1
        self.control_rate_limiter = None

    def set_geometry_builder(self, geometry_builder):
        self.geometry_builder = geometry_builder
        return self

    def set_control_parameter(self, control_parameter):
        self.control_parameter = control_parameter
        return self

    def set_control_value_index(self, control_value_index):
        self.control_value_index = control_value_index
        return self

    def set_control_increment(self, control_increment):
        self.control_increment = control_increment
        return self

    def set_control_rate_limiter(self, control_rate_limiter):
        self.control_rate_limiter = control_rate_limiter

    def build(self):
        control = HoudiniParameterControl(self.id, self.parent, self.geometry_builder, self.ui_context)
        control.set_parameter(self.control_parameter)
        control.set_value_index(self.control_value_index)
        control.set_increment(self.control_increment)
        control.set_rate_limiter(self.control_rate_limiter)

        return control
