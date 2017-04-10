class Selectable(object):
    """
    High-level definition of a selectable object.
    """

    def __init__(self):
        super(Selectable, self).__init__()

        self.selector = None
        self.is_selected = False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.get_id() == other.get_id()
        else:
            return False

    def get_id(self):
        raise NotImplementedError

    def match(self, candidate):
        raise NotImplementedError

    def on_select(self, selector, context):
        self.selector = selector
        self.is_selected = True

    def on_release(self, selector, context):
        self.selector = None
        self.is_selected = False
