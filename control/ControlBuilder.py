class ControlBuilder(object):

    def __init__(self):
        super(ControlBuilder, self).__init__()

        self.id = None
        self.parent = None
        self.ui_context = None

    def set_id(self, id):
        self.id = id
        return self

    def set_parent(self, parent):
        self.parent = parent
        return self

    def set_ui_context(self, ui_context):
        self.ui_context = ui_context
        return self

    def build(self):
        raise NotImplementedError
