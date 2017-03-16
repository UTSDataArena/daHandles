from omega import *
from cyclops import *
from euclid import *

from daInput.cursor.controller.ControllerCursor import ControllerCursor
from daInput.cursor.mocap.MocapCursor import MocapCursor
from daInput.cursor.pointer.PointerCursor import PointerCursor

from daHandles.control.Control import Control


class GenericControl(Control):

    def __init__(self, id, parent, geometry_builder, ui_context):
        super(GenericControl, self).__init__(parent, ui_context)

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

    def set_position(self, position):
        self.position = position

    def on_event(self, event):
        if self.is_selected:

            if PointerCursor.is_interested(event):
                if event.isFlagSet(EventFlags.Button1) and not event.isButtonDown(EventFlags.Button1) and not event.isButtonUp(EventFlags.Button1):
                    self.on_manipulate(event.getPosition())
                    event.setProcessed()

            elif ControllerCursor.is_interested(event):
                cursor = self.ui_context.get_cursor(event)

                if isinstance(cursor, ControllerCursor) and cursor.button1Pressed:
                    self.on_manipulate(cursor.get_position())
                    event.setProcessed()

            elif MocapCursor.is_interested(event):
                cursor = self.ui_context.get_cursor(event)

                if isinstance(cursor, MocapCursor) and cursor.pseudoButtonPressed:
                    self.on_manipulate(cursor.get_position())
                    event.setProcessed()

    def on_manipulate(self, position):
        raise NotImplementedError
