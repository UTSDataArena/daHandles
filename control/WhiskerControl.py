from daHandles.control.GenericControl import GenericControl


class WhiskerControl(GenericControl):

    def __init__(self, id, parent, geometry_builder, ui_context):
        super(WhiskerControl, self).__init__(id, parent, geometry_builder, ui_context)

    def on_manipulate(self, position):
        self.parent.on_manipulate(self, self.position, position)
        self.set_position(position)
