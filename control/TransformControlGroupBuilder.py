from daHandles.control.TransformControlGroup import TransformControlGroup
from daHandles.control.TriAxisControlGroupBuilder import TriAxisControlGroupBuilder


class TransformControlGroupBuilder(TriAxisControlGroupBuilder):

    def __init__(self):
        super(TransformControlGroupBuilder, self).__init__()

    def build(self):
        return TransformControlGroup(self.parent, self.control_builder, self.bounding_box, self.ui_context)
