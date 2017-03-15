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

    def __init__(self, id, user_id, cursor_up_image_path, cursor_down_image_path, ui_context):
        super(MocapCursor, self).__init__(id, user_id, cursor_up_image_path, cursor_down_image_path, ui_context)

        # motion capture tracking markers have no button, so we simulate a button
        # press by turning the tracking marker upside down and keeping track of
        # whether or not the press has been handled yet - this allows us to mirror
        # the behaviour of other input devices, which emit only one button down
        # event, even if the user holds the button down continuously

        self.pseudoButtonPressed = False
        self.pseudoButtonPressHandled = True

    def isButtonDown(self):

        button_down = False

        if self.pseudoButtonPressed and not self.pseudoButtonPressHandled:
            self.pseudoButtonPressHandled = True
            button_down = True

        return button_down

    def on_event(self, event):

        if MocapCursor.is_interested(event) and event.getType() == EventType.Update:

            orientation = event.getOrientation() * Vector3(0, 1, 0)

            if not self.pseudoButtonPressed and orientation[1] < MocapCursor.BUTTON_DOWN_ORIENTATION_THRESHOLD:
                self.on_button_down(event)
            elif self.pseudoButtonPressed and orientation[1] > MocapCursor.BUTTON_DOWN_ORIENTATION_THRESHOLD:
                self.on_button_up(event)
            else:
                self.on_move(event)

    def on_button_down(self, event):
        self.pseudoButtonPressed = True
        self.pseudoButtonPressHandled = False

        super(MocapCursor, self).on_button_down(event)

    def on_button_up(self, event):
        self.pseudoButtonPressed = False
        self.pseudoButtonPressHandled = True

        super(MocapCursor, self).on_button_up(event)
