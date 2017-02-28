from omega import *
from omegaToolkit import *

from daHandles.cursor.CustomImageCursor import CustomImageCursor


class ControllerCursor(CustomImageCursor):
    """
    Base class for all cursors of the controller type.
    """

    @staticmethod
    def is_interested(event):
        return event.getServiceType() == ServiceType.Controller

    def __init__(self, id, cursor_up_image_path, cursor_down_image_path, ui_context):
        super(ControllerCursor, self).__init__(id, cursor_up_image_path, cursor_down_image_path, ui_context)

    def on_event(self, event):

        if ControllerCursor.is_interested(event):

            if event.getType() == EventType.Up:
                self.on_button_up(event)
            elif event.getType() == EventType.Down:
                self.on_button_down(event)
            elif event.getType() == EventType.Update:
                self.on_move(event)
