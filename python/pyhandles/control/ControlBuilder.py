class ControlBuilder(object):

    def __init__(self):
        super(ControlBuilder, self).__init__()

        self.id = None
        self.parent = None
        self.context = None

    def set_id(self, id):
        self.id = id
        return self

    def set_parent(self, parent):
        self.parent = parent
        return self

    def set_context(self, context):
        self.context = context
        return self

    def build(self):
        raise NotImplementedError
