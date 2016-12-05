from omega import ServiceType

from daHandles.cursor.Cursor import Cursor


class PointerCursor(Cursor):
    """
    Base class for all cursors of the pointer type.
    """

    @staticmethod
    def is_interested(event):
        return event.getServiceType() == ServiceType.Pointer

    def __init__(self, id):
        super(PointerCursor, self).__init__(id)

    def on_event(self):
        pass    # no pointer specific event handling logic is currently needed
