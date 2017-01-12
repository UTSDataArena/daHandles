from cyclops import *

from daHandles.control.geometry.ControlGeometryBuilder import ControlGeometryBuilder


class SphereControlGeometryBuilder(ControlGeometryBuilder):

    DEFAULT_RADIUS = 0.25
    DEFAULT_SUBDIVISIONS = 1

    def __init__(self):
        super(SphereControlGeometryBuilder, self).__init__()

        self.radius = SphereControlGeometryBuilder.DEFAULT_RADIUS
        self.subdivisions = SphereControlGeometryBuilder.DEFAULT_SUBDIVISIONS

    def set_radius(self, radius):
        self.radius = radius
        return self

    def set_subdivisions(self, subdivisions):
        self.subdivisions = subdivisions
        return self

    def build(self):
        return SphereShape.create(self.radius, self.subdivisions)