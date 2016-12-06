from omega import *

from daHandles.selection.Selectable import Selectable


class SelectableSceneNode(Selectable):

    def __init__(self, name, geo=None):
        super(SelectableSceneNode, self).__init__()

        self.node = SceneNode.create(name)

        self.geo = geo
        self.geo.setName('%s.geo' % name)
        self.geo.setSelectable(True)

        self.node.addChild(self.geo)

    def get_id(self):
        return self.node.getName()

    def get_geo(self):
        return self.geo

    def match(self, candidate):
        return [self] if self.geo.getName() == candidate.getName() else []
