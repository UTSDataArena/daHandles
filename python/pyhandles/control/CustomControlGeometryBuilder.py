from cyclops import *
from omega import *

from pyhandles.control.ControlGeometryBuilder import ControlGeometryBuilder


class CustomControlGeometryBuilder(ControlGeometryBuilder):

    def __init__(self):
        super(CustomControlGeometryBuilder, self).__init__()

        self.name = None
        self.path = None

    def set_name(self, name):
        self.name = name
        return self

    def set_path(self, path):
        self.path = path
        return self

    def build(self):
        model = ModelInfo()
        model.name = self.name
        model.path = self.path
        model.optimize = False

        getSceneManager().loadModel(model)

        return StaticObject.create(self.name)