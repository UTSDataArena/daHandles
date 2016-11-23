from pyhandles.cursor.Cursor import Cursor


class PointerCursor(Cursor):
    """
    Base class for all cursors of the pointer type.
    """

    def __init__(self, id):
        super(PointerCursor, self).__init__(id)

    def on_event(self):
        pass    # no pointer specific event handling logic is currently needed
