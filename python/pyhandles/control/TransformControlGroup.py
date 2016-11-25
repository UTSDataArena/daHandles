from cyclops import *
from omega import *

from pyhandles.control.RotateControlGroup import Rotation
from pyhandles.control.ScaleControlGroup import Scale
from pyhandles.control.TranslateControlGroup import Translation
from pyhandles.control.TriAxisControlGroup import TriAxisControlGroup


class TransformControlGroup(TriAxisControlGroup):

    SCALE = 's'
    ROTATE = 'r'
    TRANSLATE = 't'

    def __init__(self, parent, builder, ui_context):
        super(TransformControlGroup, self).__init__(parent, builder, ui_context)

        self.id = '%s.scale' % parent.get_id()

        self.build()
        self.set_visible(False)

        self.mode = None

    def build(self):
        super(TransformControlGroup, self).build()

        setEventFunction(self.on_event)

    def on_event(self):
        if self.is_selected:
            event = getEvent()

            if event.getServiceType() == ServiceType.Keyboard:
                if event.isKeyDown(ord(TransformControlGroup.SCALE)):
                    self.mode = TransformControlGroup.SCALE
                elif event.isKeyUp(ord(TransformControlGroup.SCALE)):
                    self.mode = None
                elif event.isKeyDown(ord(TransformControlGroup.ROTATE)):
                    self.mode = TransformControlGroup.ROTATE
                elif event.isKeyUp(ord(TransformControlGroup.ROTATE)):
                    self.mode = None
                elif event.isKeyDown(ord(TransformControlGroup.TRANSLATE)):
                    self.mode = TransformControlGroup.TRANSLATE
                elif event.isKeyUp(ord(TransformControlGroup.TRANSLATE)):
                    self.mode = None

    def on_manipulate(self, control, origin, movement):

        if self.mode == TransformControlGroup.SCALE:

            # our current strategy to ensure that controls do not get obscured by the
            # rescaled geometry is to also adjust the scale of the control so that it
            # remains visible - a better long term strategy would be to determine the
            # bounds of the geometry and draw the controls on the surface of this volume

            object_scale, handle_scale = Scale.scale(self.get_control_axis(control), origin, self.parent.get_geo().getScale(), control.get_geo().getScale(), movement)

            control.get_geo().setScale(handle_scale)
            self.parent.get_geo().setScale(object_scale)

        elif self.mode == TransformControlGroup.ROTATE:
            axis, angle = Rotation.rotate(self.get_control_axis(control), origin, movement)
            self.parent.node.rotate(axis, angle, Space.Local)

        elif self.mode == TransformControlGroup.TRANSLATE:
            self.parent.node.translate(Translation.translate(self.get_control_axis(control), origin, movement), Space.Local)
