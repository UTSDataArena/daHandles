from cyclops import *

from daHandles.control.ControlGeometryBuilder import ControlGeometryBuilder


class CylinderControlGeometryBuilder(ControlGeometryBuilder):

    DEFAULT_LENGTH = 0.5
    DEFAULT_RADIUS1 = 0.05
    DEFAULT_RADIUS2 = 0.05
    DEFAULT_SUBDIVISIONS = 1
    DEFAULT_SIDES = 16

    def __init__(self):
        super(CylinderControlGeometryBuilder, self).__init__()

        self.length = CylinderControlGeometryBuilder.DEFAULT_LENGTH
        self.radius1 = CylinderControlGeometryBuilder.DEFAULT_RADIUS1
        self.radius2 = CylinderControlGeometryBuilder.DEFAULT_RADIUS2
        self.subdivisions = CylinderControlGeometryBuilder.DEFAULT_SUBDIVISIONS
        self.sides = CylinderControlGeometryBuilder.DEFAULT_SIDES

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
        return CylinderShape.create(self.length, self.radius1, self.radius2, self.subdivisions, self.sides)