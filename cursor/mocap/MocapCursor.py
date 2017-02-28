from euclid import *
from omega import *
from omegaToolkit import *

from daHandles.cursor.CustomImageCursor import CustomImageCursor


class MocapCursor(CustomImageCursor):
    """
    Base class for all cursors of the mocap type.
    """

    BUTTON_DOWN_ORIENTATION_THRESHOLD = -0.6

    @staticmethod
    def is_interested(event):
        return event.getServiceType() == ServiceType.Mocap

    def __init__(self, id, cursor_up_image_path, cursor_down_image_path, ui_context):
        super(MocapCursor, self).__init__(id, cursor_up_image_path, cursor_down_image_path, ui_context)

        self.pseudoButtonPressed = False

    def on_event(self, event):

        if MocapCursor.is_interested(event) and event.getType() == EventType.Update:

            orientation = event.getOrientation() * Vector3(0, 1, 0)

            if not self.pseudoButtonPressed and orientation[1] < MocapCursor.BUTTON_DOWN_ORIENTATION_THRESHOLD:
                self.pseudoButtonPressed = True
                self.on_button_down(event)
            elif self.pseudoButtonPressed and orientation[1] > MocapCursor.BUTTON_DOWN_ORIENTATION_THRESHOLD:
                self.pseudoButtonPressed = False
                self.on_button_up(event)
            else:
                self.on_move(event)
