from cyclops import *
from euclid import *
from omega import *

from daHandles.control.ControlGroup import ControlGroup


class SingleControlGroup(ControlGroup):

    def __init__(self, parent, builder, ui_context):
        super(SingleControlGroup, self).__init__(parent, ui_context)

        self.id = None
        self.control = None
        self.builder = builder

        self.build()
        self.set_visible(False)

    def build(self):

        self.control = self.builder.set_id('control').set_parent(self).set_ui_context(self.ui_context).build()
        self.control.set_effect('colored -d red')

        self.controls.append(self.control)

    def get_id(self):
        return self.id

    def on_manipulate(self, control, origin, movement):
        super(SingleControlGroup, self).on_manipulate(control, origin, movement)
