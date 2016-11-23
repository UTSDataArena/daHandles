from euclid import *
from omega import *
from omegaToolkit import *

from pyhandles.cursor.Cursor import Cursor


class ControllerCursor(Cursor):
    """
    Base class for all cursors of the controller type.
    """

    def __init__(self, id, container, cursor_image_path):
        super(ControllerCursor, self).__init__(id)

        self.container = container

        self.cursor = Image.create(container)
        self.cursor.setSize(Vector2(Cursor.DEFAULT_SIZE, Cursor.DEFAULT_SIZE))
        self.cursor.setData(loadImage(cursor_image_path))

    def get_position(self):
        return self.cursor.getPosition()

    def set_position(self, position):
        self.cursor.setPosition(position)

    def on_event(self):

        event = getEvent()

        if event.getServiceType() == ServiceType.Controller:
            if event.getType() == EventType.Up:
                self.on_button_up(event)
            elif event.getType() == EventType.Down:
                self.on_button_down(event)
            elif event.getType() == EventType.Move:
                self.on_move(event)

    def on_move(self, event):
        raise NotImplementedError

    def on_button_up(self, event):
        raise NotImplementedError

    def on_button_down(self, event):
        raise NotImplementedError
