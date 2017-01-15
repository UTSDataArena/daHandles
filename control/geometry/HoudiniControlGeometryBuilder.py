from cyclops import *

from daHandles.control.geometry.ControlGeometryBuilder import ControlGeometryBuilder


class HoudiniControlGeometryBuilder(ControlGeometryBuilder):

    def __init__(self):
        super(HoudiniControlGeometryBuilder, self).__init__()

        self.engine = None

        self.otl_path = None
        self.asset_name = None
        self.geometry_name = None

    def set_engine(self, engine):
        self.engine = engine
        return self

    def set_otl_path(self, otl_path):
        self.otl_path = otl_path
        return self

    def set_asset_name(self, asset_name):
        self.asset_name = asset_name
        return self

    def set_geometry_name(self, geometry_name):
        self.geometry_name = geometry_name
        return self

    def build(self):
        self.engine.loadAssetLibraryFromFile(self.otl_path)
        self.engine.instantiateAsset(self.asset_name)
        self.engine.instantiateGeometry(self.geometry_name)

        return StaticObject.create(self.geometry_name)
