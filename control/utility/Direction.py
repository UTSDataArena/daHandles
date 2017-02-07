from daHandles.control.utility.Axis import Axis


class Direction(object):

    POSITIVE = 1
    NEGATIVE = -1

    @staticmethod
    def get_x_direction(origin, movement):
        return Direction.NEGATIVE if movement.x <= origin.x else Direction.POSITIVE

    @staticmethod
    def get_y_direction(origin, movement):
        return Direction.POSITIVE if movement.y <= origin.y else Direction.NEGATIVE

    @staticmethod
    def get_z_direction(origin, movement):
        return Direction.POSITIVE if movement.x <= origin.x else Direction.NEGATIVE

    @staticmethod
    def get_direction(axis, origin, movement):
        if axis == Axis.X_AXIS:
            return Direction.get_x_direction(origin, movement)
        elif axis == Axis.Y_AXIS:
            return Direction.get_y_direction(origin, movement)
        elif axis == Axis.Z_AXIS:
            return Direction.get_z_direction(origin, movement)
        else:
            raise ValueError('Axis value is unsupported: %s' % axis)
