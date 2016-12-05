from daHandles.selection.Selectable import Selectable


class Control(Selectable):
    """
    Base class for all control implementations.
    """

    def __init__(self, parent, ui_context):
        super(Control, self).__init__()

        self.parent = parent
        self.ui_context = ui_context

    def build(self):
        raise NotImplementedError

    def get_id(self):
        super(Control, self).get_id()

    def get_geo(self):
        raise NotImplementedError

    def set_visible(self, visible):
        raise NotImplementedError

    def match(self, candidate):
        super(Control, self).match(candidate)

    def show(self):
        self.set_visible(True)

    def hide(self):
        self.set_visible(False)

    def on_select(self, context):
        super(Control, self).on_select(context)

    def on_release(self, context):
        super(Control, self).on_release(context)
