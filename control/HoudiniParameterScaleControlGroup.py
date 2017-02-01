from daHandles.control.ScaleControlGroup import ScaleControlGroup


class HoudiniParameterScaleControlGroup(ScaleControlGroup):

    def __init__(self, parent, builder, bounding_box, ui_context, parameter_mapping):

        self.parameter_mapping = parameter_mapping

        super(HoudiniParameterScaleControlGroup, self).__init__(parent, builder, bounding_box, ui_context)

    def build_control(self, id):
        return self.builder.set_id(id).set_parent(self).set_ui_context(self.ui_context).set_control_parameter(self.parameter_mapping[id]).build()
