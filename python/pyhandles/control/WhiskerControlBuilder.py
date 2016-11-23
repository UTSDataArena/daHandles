from pyhandles.control.ControlBuilder import ControlBuilder
from pyhandles.control.WhiskerControl import WhiskerControl


class WhiskerControlBuilder(ControlBuilder):

    def __init__(self):
        super(WhiskerControlBuilder, self).__init__()

        self.length = WhiskerControl.DEFAULT_LENGTH
        self.radius1 = WhiskerControl.DEFAULT_RADIUS1
        self.radius2 = WhiskerControl.DEFAULT_RADIUS2
        self.subdivisions = WhiskerControl.DEFAULT_SUBDIVISIONS
        self.sides = WhiskerControl.DEFAULT_SIDES

    def set_length(self, length):
        self.length = length
        return self

    def set_radius1(self, radius1):
        self.radius1 = radius1
        return self

    def set_radius2(self, radius2):
        self.radius2 = radius2
        return self

    def set_subdivisions(self, subdivisions):
        self.subdivisions = subdivisions
        return self

    def set_sides(self, sides):
        self.sides = sides
        return self

    def build(self):
        return WhiskerControl(self.id, self.parent, self.context, self.length, self.radius1, self.radius2, self.subdivisions, self.sides)
