from omega import *
from omegaToolkit import *

from daHandles.cursor.pointer.MousePointerCursor import MousePointerCursor


class UiContext(object):

    def __init__(self):
        super(UiContext, self).__init__()

        self.container = None

        self.pointer = MousePointerCursor('mouse')
        self.cursors = []

        self.build()

    def build(self):
        ui = UiModule.createAndInitialize()
        self.container = Container.create(ContainerLayout.LayoutFree, ui.getUi())

    def get_cursor(self, event):
        return self.cursors[event.getUserId()]

    def add_cursor(self, cursor):
        self.cursors.append(cursor)
        setEventFunction(cursor.on_event)
