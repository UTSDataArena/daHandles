from pyhandles.control.ControlBuilder import ControlBuilder
from pyhandles.control.TranslateControlGroup import TranslateControlGroup


class TranslateControlGroupBuilder(ControlBuilder):

    def __init__(self):
        super(TranslateControlGroupBuilder, self).__init__()

        self.control_builder = None

    def set_control_builder(self, control_builder):
        self.control_builder = control_builder
        return self

    def build(self):
        return TranslateControlGroup(self.parent, self.context, self.control_builder)
