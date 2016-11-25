from pyhandles.control.ControlBuilder import ControlBuilder
from pyhandles.control.TransformControlGroup import TransformControlGroup


class TransformControlGroupBuilder(ControlBuilder):

    def __init__(self):
        super(TransformControlGroupBuilder, self).__init__()

        self.control_builder = None

    def set_control_builder(self, control_builder):
        self.control_builder = control_builder
        return self

    def build(self):
        return TransformControlGroup(self.parent, self.control_builder, self.ui_context)
