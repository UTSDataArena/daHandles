from daHandles.control.ScaleControlGroup import ScaleControlGroup
from daHandles.control.TriAxisControlGroupBuilder import TriAxisControlGroupBuilder


class ScaleControlGroupBuilder(TriAxisControlGroupBuilder):

    def __init__(self):
        super(ScaleControlGroupBuilder, self).__init__()

    def build(self):
        return ScaleControlGroup(self.parent, self.control_builder, self.bounding_box, self.ui_context)
