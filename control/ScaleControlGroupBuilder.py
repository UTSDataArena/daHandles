from daHandles.control.ControlBuilder import ControlBuilder
from daHandles.control.ScaleControlGroup import ScaleControlGroup


class ScaleControlGroupBuilder(ControlBuilder):

    def __init__(self):
        super(ScaleControlGroupBuilder, self).__init__()

        self.control_builder = None

    def set_control_builder(self, control_builder):
        self.control_builder = control_builder
        return self

    def build(self):
        return ScaleControlGroup(self.parent, self.control_builder, self.ui_context)
