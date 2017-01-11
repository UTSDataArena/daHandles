from daHandles.control.ControlBuilder import ControlBuilder
from daHandles.control.SingleControlGroup import SingleControlGroup


class SingleControlGroupBuilder(ControlBuilder):

    def __init__(self):
        super(SingleControlGroupBuilder, self).__init__()

        self.control_builder = None

    def set_control_builder(self, control_builder):
        self.control_builder = control_builder
        return self

    def build(self):
        return SingleControlGroup(self.parent, self.control_builder, self.ui_context)
