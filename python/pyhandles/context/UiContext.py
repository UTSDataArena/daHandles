from omega import *
from omegaToolkit import *


class UiContext(object):

    def __init__(self):
        super(UiContext, self).__init__()

        self.container = None
        self.cursors = []

        self.build()

    def build(self):
        ui = UiModule.createAndInitialize()
        self.container = Container.create(ContainerLayout.LayoutFree, ui.getUi())

    def add_cursor(self, cursor):
        self.cursors.append(cursor)
        setEventFunction(cursor.on_event)
