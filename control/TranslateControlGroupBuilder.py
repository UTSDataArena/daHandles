from daHandles.control.TranslateControlGroup import TranslateControlGroup
from daHandles.control.TriAxisControlGroupBuilder import TriAxisControlGroupBuilder


class TranslateControlGroupBuilder(TriAxisControlGroupBuilder):

    def __init__(self):
        super(TranslateControlGroupBuilder, self).__init__()

    def build(self):
        return TranslateControlGroup(self.parent, self.control_builder, self.bounding_box, self.ui_context)
