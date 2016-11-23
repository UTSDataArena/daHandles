class Cursor(object):
    """
    High-level implementation of a cyclops cursor driven by the VRPN framework.
    """

    DEFAULT_SIZE = 24

    def __init__(self, id):
        """
        Initialise the cursor.

        :param id: An identifier to distinguish this cursor from others in the scene.
        """
        super(Cursor, self).__init__()

        self.id = id

    def on_event(self):
        """
        Respond to input events.

        Register this method using the omegalib setEventFunction in order to
        connect it to the application event stream.
        """
        raise NotImplementedError
