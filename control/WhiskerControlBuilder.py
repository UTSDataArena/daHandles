from daHandles.control.ControlBuilder import ControlBuilder
from daHandles.control.WhiskerControl import WhiskerControl


class WhiskerControlBuilder(ControlBuilder):

    def __init__(self):
        super(WhiskerControlBuilder, self).__init__()

        self.geometry_builder = None

    def set_geometry_builder(self, geometry_builder):
        self.geometry_builder = geometry_builder
        return self

    def build(self):
        return WhiskerControl(self.id, self.parent, self.geometry_builder, self.ui_context)
