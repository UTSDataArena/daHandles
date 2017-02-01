from daHandles.control.ScaleControlGroupBuilder import ScaleControlGroupBuilder
from daHandles.control.HoudiniParameterScaleControlGroup import HoudiniParameterScaleControlGroup


class HoudiniParameterScaleControlGroupBuilder(ScaleControlGroupBuilder):

    def __init__(self):
        super(HoudiniParameterScaleControlGroupBuilder, self).__init__()

        self.parameter_mapping = {}

    def set_parameter_mapping(self, parameter_mapping):
        self.parameter_mapping = parameter_mapping
        return self

    def build(self):
        return HoudiniParameterScaleControlGroup(self.parent, self.control_builder, self.bounding_box, self.ui_context, self.parameter_mapping)
