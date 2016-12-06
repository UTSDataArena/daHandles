from daHandles.control.ControlBuilder import ControlBuilder
from daHandles.control.TransformControlGroup import TransformControlGroup


class TransformControlGroupBuilder(ControlBuilder):

    def __init__(self):
        super(TransformControlGroupBuilder, self).__init__()

        self.bounding_box = None
        self.control_builder = None

    def set_bounding_box(self, bounding_box):
        self.bounding_box = bounding_box
        return self

    def set_control_builder(self, control_builder):
        self.control_builder = control_builder
        return self

    def build(self):
        return TransformControlGroup(self.parent, self.control_builder, self.bounding_box, self.ui_context)
