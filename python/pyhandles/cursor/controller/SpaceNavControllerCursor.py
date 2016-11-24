from cyclops import *
from euclid import *
from omega import *


from pyhandles.cursor.controller.ControllerCursor import ControllerCursor


class SpaceNavControllerCursor(ControllerCursor):

    MOTION_MULTIPLIER = 3   # spacenav motion is very fine-grained

    def __init__(self, id, cursor_image_path, ui_context):
        super(SpaceNavControllerCursor, self).__init__(id, cursor_image_path, ui_context)

        self.button1Pressed = False
        self.button2Pressed = False

    def on_move(self, event):

        if event.getExtraDataItems() >= 2:

            dx = event.getExtraDataFloat(0)
            dy = event.getExtraDataFloat(1)

            x = self.cursor.getPosition().x + (dx * SpaceNavControllerCursor.MOTION_MULTIPLIER)
            y = self.cursor.getPosition().y + (dy * SpaceNavControllerCursor.MOTION_MULTIPLIER)

            position = Vector2(self.cursor.getPosition().x, self.cursor.getPosition().y)

            position.x = x
            position.y = y

            self.set_position(position)

    def on_button_up(self, event):

        if event.isButtonUp(EventFlags.Button1):
            self.button1Pressed = False
        elif event.isButtonUp(EventFlags.Button2):
            self.button2Pressed = False

    def on_button_down(self, event):

        if event.isButtonDown(EventFlags.Button1):
            self.button1Pressed = True
        elif event.isButtonDown(EventFlags.Button2):
            self.button2Pressed = True
