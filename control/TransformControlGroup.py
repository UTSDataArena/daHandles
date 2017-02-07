from cyclops import *
from euclid import *
from omega import *

from daHandles.control.RotateControlGroup import Rotation
from daHandles.control.ScaleControlGroup import Scale
from daHandles.control.TranslateControlGroup import Translation
from daHandles.control.TriAxisControlGroup import TriAxisControlGroup
from daHandles.control.utility.Axis import Axis
from daHandles.control.utility.Direction import Direction


class TransformControlGroup(TriAxisControlGroup):

    SCALE = 's'
    ROTATE = 'r'
    TRANSLATE = 't'

    def __init__(self, parent, builder, bounding_box, ui_context):
        super(TransformControlGroup, self).__init__(parent, builder, bounding_box, ui_context)

        self.id = '%s.scale' % parent.get_id()

        self.build()
        self.set_visible(False)

        self.mode = None

    def build(self):
        super(TransformControlGroup, self).build()

    def on_event(self):
        super(TransformControlGroup, self).on_event()

        if self.is_selected:
            event = getEvent()

            if event.getServiceType() == ServiceType.Keyboard:

                if event.isKeyDown(ord(TransformControlGroup.SCALE)):
                    self.mode = TransformControlGroup.SCALE
                    event.setProcessed()

                elif event.isKeyUp(ord(TransformControlGroup.SCALE)):
                    self.mode = None
                    event.setProcessed()

                elif event.isKeyDown(ord(TransformControlGroup.ROTATE)):
                    self.mode = TransformControlGroup.ROTATE
                    event.setProcessed()

                elif event.isKeyUp(ord(TransformControlGroup.ROTATE)):
                    self.mode = None
                    event.setProcessed()

                elif event.isKeyDown(ord(TransformControlGroup.TRANSLATE)):
                    self.mode = TransformControlGroup.TRANSLATE
                    event.setProcessed()

                elif event.isKeyUp(ord(TransformControlGroup.TRANSLATE)):
                    self.mode = None
                    event.setProcessed()

    def on_manipulate(self, control, origin, movement):

        if self.mode == TransformControlGroup.SCALE:
            axis = self.get_control_axis(control)
            direction = Direction.get_direction(axis, origin, movement)

            self.parent.get_geo().setScale(self.parent.get_geo().getScale() + Scale.scale(axis, origin, movement))

            if axis == Axis.X_AXIS:
                control.get_geo().translate(Vector3(Scale.INCREMENT / 2 * direction, 0, 0), Space.Parent)
            elif axis == Axis.Y_AXIS:
                control.get_geo().translate(Vector3(0, Scale.INCREMENT / 2 * direction, 0), Space.Parent)
            elif axis == Axis.Z_AXIS:
                control.get_geo().translate(Vector3(0, 0, Scale.INCREMENT / 2 * direction), Space.Parent)

        elif self.mode == TransformControlGroup.ROTATE:
            axis, angle = Rotation.rotate(self.get_control_axis(control), origin, movement)
            self.parent.node.rotate(axis, angle, Space.Local)

        elif self.mode == TransformControlGroup.TRANSLATE:
            self.parent.node.translate(Translation.translate(self.get_control_axis(control), origin, movement), Space.Local)
