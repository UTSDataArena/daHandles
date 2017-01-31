from daHandles.control.ControlBuilder import ControlBuilder


class TriAxisControlGroupBuilder(ControlBuilder):

    def __init__(self):
        super(TriAxisControlGroupBuilder, self).__init__()

        self.bounding_box = None
        self.control_builder = None

    def set_bounding_box(self, bounding_box):
        self.bounding_box = bounding_box
        return self

    def set_control_builder(self, control_builder):
        self.control_builder = control_builder
        return self

    def build(self):
        raise NotImplementedError