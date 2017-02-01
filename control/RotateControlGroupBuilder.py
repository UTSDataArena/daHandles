from daHandles.control.RotateControlGroup import RotateControlGroup
from daHandles.control.TriAxisControlGroupBuilder import TriAxisControlGroupBuilder


class RotateControlGroupBuilder(TriAxisControlGroupBuilder):

    def __init__(self):
        super(RotateControlGroupBuilder, self).__init__()

    def build(self):
        return RotateControlGroup(self.parent, self.control_builder, self.bounding_box, self.ui_context)
