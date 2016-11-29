from omega import *
from cyclops import *
from euclid import *

from pyhandles.control.Control import Control
from pyhandles.cursor.controller.ControllerCursor import ControllerCursor
from pyhandles.cursor.pointer.PointerCursor import PointerCursor


class WhiskerControl(Control):

    def __init__(self, id, parent, geometry_builder, ui_context):
        super(WhiskerControl, self).__init__(parent, ui_context)

        self.id = id
        self.geometry_builder = geometry_builder
        self.geo = None

        self.position = Vector2(0, 0)

        self.build()
        self.set_visible(False)

    def build(self):
        self.geo = self.geometry_builder.build()
        self.geo.setName('%s.%s' % (self.parent.get_id(), self.id))
        self.geo.setSelectable(True)

    def match(self, candidate):
        return [self] if self.get_id() == candidate.getName() else []

    def get_id(self):
        return self.geo.getName()

    def get_geo(self):
        return self.geo

    def set_visible(self, visible):
        self.geo.setVisible(visible)

    def set_effect(self, effect):
        self.geo.setEffect(effect)

    def on_event(self):
        if self.is_selected:
            event = getEvent()
            if PointerCursor.is_interested(event):
                if event.isFlagSet(EventFlags.Button1) and not event.isButtonDown(EventFlags.Button1) and not event.isButtonUp(EventFlags.Button1):
                    self.on_manipulate(event.getPosition())

            elif ControllerCursor.is_interested(event):
                cursor = self.ui_context.get_cursor(event)

                if isinstance(cursor, ControllerCursor) and cursor.button1Pressed:
                    self.on_manipulate(cursor.get_position())

    def on_manipulate(self, position):
        self.parent.on_manipulate(self, self.position, position)
        self.position = position
