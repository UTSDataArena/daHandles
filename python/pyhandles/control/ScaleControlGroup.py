from pyhandles.control.TriAxisControlGroup import TriAxisControlGroup


class Scale(object):

    INCREMENT = 0.1

    # @todo: eliminate special logic for handles scaling once an improved strategy is in place

    @staticmethod
    def scale(axis, origin, object_current, handle_current, delta):

        object_scale = object_current
        handle_scale = handle_current

        if axis == TriAxisControlGroup.X_AXIS:
            if delta.x <= origin.x:
                object_scale.x -= Scale.INCREMENT
                handle_scale.z -= Scale.INCREMENT * 0.5
            else:
                object_scale.x += Scale.INCREMENT
                handle_scale.z += Scale.INCREMENT * 0.5

        elif axis == TriAxisControlGroup.Y_AXIS:
            if delta.y <= origin.y:
                object_scale.y += Scale.INCREMENT
                handle_scale.z += Scale.INCREMENT * 0.5
            else:
                object_scale.y -= Scale.INCREMENT
                handle_scale.z -= Scale.INCREMENT * 0.5

        elif axis == TriAxisControlGroup.Z_AXIS:
            if delta.x <= origin.x:
                object_scale.z += Scale.INCREMENT
                handle_scale.z += Scale.INCREMENT * 0.5
            else:
                object_scale.z -= Scale.INCREMENT
                handle_scale.z -= Scale.INCREMENT * 0.5

        return object_scale, handle_scale


class ScaleControlGroup(TriAxisControlGroup):

    def __init__(self, parent, builder, ui_context):
        super(ScaleControlGroup, self).__init__(parent, builder, ui_context)

        self.id = '%s.scale' % parent.get_id()

        self.build()
        self.set_visible(False)

    def on_manipulate(self, control, origin, movement):

        # our current strategy to ensure that controls do not get obscured by the
        # rescaled geometry is to also adjust the scale of the control so that it
        # remains visible - a better long term strategy would be to determine the
        # bounds of the geometry and draw the controls on the surface of this volume

        object_scale, handle_scale = Scale.scale(self.get_control_axis(control), origin, self.parent.get_geo().getScale(), control.get_geo().getScale(), movement)

        control.get_geo().setScale(handle_scale)
        self.parent.get_geo().setScale(object_scale)
