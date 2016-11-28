from omega import *
from cyclops import *
from euclid import *

from pyhandles.control.Control import Control
from pyhandles.cursor.controller.ControllerCursor import ControllerCursor
from pyhandles.cursor.pointer.PointerCursor import PointerCursor


class WhiskerControl(Control):

    DEFAULT_LENGTH = 0.5
    DEFAULT_RADIUS1 = 0.05
    DEFAULT_RADIUS2 = 0.05
    DEFAULT_SUBDIVISIONS = 1
    DEFAULT_SIDES = 16

    def __init__(self, id, parent, ui_context, length=DEFAULT_LENGTH, radius1=DEFAULT_RADIUS1, radius2=DEFAULT_RADIUS2, subdivisions=DEFAULT_SUBDIVISIONS, sides=DEFAULT_SIDES):
        super(WhiskerControl, self).__init__(parent, ui_context)

        self.id = id
        self.length = length
        self.radius1 = radius1
        self.radius2 = radius2
        self.subdivisions = subdivisions
        self.sides = sides
        self.geo = None

        self.position = Vector2(0, 0)

        self.build()
        self.set_visible(False)

    def build(self):
        self.geo = CylinderShape.create(self.length, self.radius1, self.radius2, self.subdivisions, self.sides)
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
