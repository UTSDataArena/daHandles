from cyclops import *
from euclid import *
from omega import *


from daHandles.cursor.mocap.MocapCursor import MocapCursor


class OptiTrackMocapCursor(MocapCursor):

    def __init__(self, id, user_id, cursor_up_image_path, cursor_down_image_path, ui_context):
        super(OptiTrackMocapCursor, self).__init__(id, user_id, cursor_up_image_path, cursor_down_image_path, ui_context)

    def on_move(self, event):

        if event.getExtraDataItems() >= 2:

            # TODO: this implementation is a guess - confirm actual behaviour

            x = event.getExtraDataInt(0)
            y = event.getExtraDataInt(1)

            self.set_position(Vector2(x, y))

    def on_button_up(self, event):
        super(OptiTrackMocapCursor, self).on_button_up(event)

        pass    # TODO: add custom optitrack marker specific button up logic here

    def on_button_down(self, event):
        super(OptiTrackMocapCursor, self).on_button_down(event)

        pass    # TODO: add custom optitrack marker specific button down logic here
