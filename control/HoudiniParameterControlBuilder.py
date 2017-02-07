from daHandles.control.ControlBuilder import ControlBuilder
from daHandles.control.HoudiniParameterControl import HoudiniParameterControl


class HoudiniParameterControlBuilder(ControlBuilder):

    def __init__(self):
        super(HoudiniParameterControlBuilder, self).__init__()

        self.geometry_builder = None
        self.parameter = None
        self.value_index = 0
        self.increment = 1
        self.rate_limiter = None
        self.min_value = None
        self.max_value = None

    def set_geometry_builder(self, geometry_builder):
        self.geometry_builder = geometry_builder
        return self

    def set_parameter(self, parameter):
        self.parameter = parameter
        return self

    def set_value_index(self, value_index):
        self.value_index = value_index
        return self

    def set_increment(self, increment):
        self.increment = increment
        return self

    def set_rate_limiter(self, rate_limiter):
        self.rate_limiter = rate_limiter
        return self

    def set_min_value(self, min_value):
        self.min_value = min_value
        return self

    def set_max_value(self, max_value):
        self.max_value = max_value
        return self

    def build(self):
        control = HoudiniParameterControl(self.id, self.parent, self.geometry_builder, self.ui_context)
        control.set_parameter(self.parameter)
        control.set_value_index(self.value_index)
        control.set_increment(self.increment)
        control.set_rate_limiter(self.rate_limiter)
        control.set_min_value(self.min_value)
        control.set_max_value(self.max_value)

        return control
