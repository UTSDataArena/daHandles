class Selectable(object):
    """
    High-level definition of a selectable object.
    """

    def __init__(self):
        super(Selectable, self).__init__()

        self.is_selected = False

    def get_id(self):
        raise NotImplementedError

    def match(self, candidate):
        raise NotImplementedError

    def on_select(self, context):
        self.is_selected = True

    def on_release(self, context):
        self.is_selected = False