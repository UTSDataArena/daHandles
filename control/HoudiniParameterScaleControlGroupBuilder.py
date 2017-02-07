from daHandles.control.ScaleControlGroupBuilder import ScaleControlGroupBuilder
from daHandles.control.HoudiniParameterScaleControlGroup import HoudiniParameterScaleControlGroup


class HoudiniParameterScaleControlGroupBuilder(ScaleControlGroupBuilder):

    def __init__(self):
        super(HoudiniParameterScaleControlGroupBuilder, self).__init__()

        self.parameter_mapping = {}

        self.min_value = None
        self.max_value = None

    def set_parameter_mapping(self, parameter_mapping):
        self.parameter_mapping = parameter_mapping
        return self

    def set_min_value(self, min_value):
        self.min_value = min_value
        return self

    def set_max_value(self, max_value):
        self.max_value = max_value
        return self

    def build(self):
        control = HoudiniParameterScaleControlGroup(self.parent, self.control_builder, self.bounding_box, self.ui_context, self.parameter_mapping)
        control.set_min_value(self.min_value)
        control.set_max_value(self.max_value)

        return control
