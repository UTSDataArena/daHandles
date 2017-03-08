from euclid import *
from omega import *
from omegaToolkit import *

from daHandles.cursor.pointer.MousePointerCursor import MousePointerCursor


class UiContext(object):

    def __init__(self):
        super(UiContext, self).__init__()

        self.ui = None
        self.container = None

        self.pointer = MousePointerCursor('mouse')
        self.cursors = []

        self.build()

    def build(self):
        self.ui = UiModule.createAndInitialize()

        size = getDisplayPixelSize()

        self.container = Container.create(ContainerLayout.LayoutFree, self.ui.getUi())
        self.container.setAutosize(False)
        self.container.setSize(Vector2(size[0], size[1] / 2))

        settings = self.container.get3dSettings()

        settings.enable3d = True
        settings.position = Vector3(-6, 2.6, -2.4)
        settings.scale = 0.001
        settings.node = getScene()

    def get_cursor(self, event):
        for cursor in self.cursors:
            if cursor.get_user_id() == event.getUserId():
                return cursor

    def add_cursor(self, cursor):
        self.cursors.append(cursor)

    def on_event(self, event):
        for cursor in self.cursors:
            cursor.on_event(event)
