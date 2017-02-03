from euclid import *
from omega import *
from omegaToolkit import *

from daHandles.cursor.Cursor import Cursor


class CustomImageCursor(Cursor):

    @staticmethod
    def load_image(path):
        return loadImage(path) if path else None

    def __init__(self, id, cursor_up_image_path, cursor_down_image_path, ui_context):
        super(CustomImageCursor, self).__init__(id)

        self.ui_context = ui_context

        self.cursor = Image.create(self.ui_context.container)
        self.cursor.setSize(Vector2(Cursor.DEFAULT_SIZE, Cursor.DEFAULT_SIZE))

        self.cursor_up_image = CustomImageCursor.load_image(cursor_up_image_path)
        self.cursor_down_image = CustomImageCursor.load_image(cursor_down_image_path)

        if self.cursor_up_image:
            self.cursor.setData(self.cursor_up_image)

    def get_position(self):
        return self.cursor.getPosition()

    def set_position(self, position):
        self.cursor.setPosition(position)

    def on_move(self, event):
        raise NotImplementedError

    def on_button_up(self, event):
        self.cursor.setData(self.cursor_up_image)

    def on_button_down(self, event):
        self.cursor.setData(self.cursor_down_image)
