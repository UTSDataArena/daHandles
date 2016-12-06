from daHandles.control.ControlBuilder import ControlBuilder
from daHandles.control.RotateControlGroup import RotateControlGroup


class RotateControlGroupBuilder(ControlBuilder):

    def __init__(self):
        super(RotateControlGroupBuilder, self).__init__()

        self.control_builder = None

    def set_control_builder(self, control_builder):
        self.control_builder = control_builder
        return self

    def build(self):
        return RotateControlGroup(self.parent, self.control_builder, self.ui_context)
