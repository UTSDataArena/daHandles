from daHandles.control.GenericControl import GenericControl
from daHandles.control.utility.Direction import Direction


class HoudiniParameter:

    HAPI_PARMTYPE_INT = 0
    HAPI_PARMTYPE_MULTIPARM_LIST = 1
    HAPI_PARMTYPE_TOGGLE = 2
    HAPI_PARMTYPE_BUTTON = 3
    HAPI_PARMTYPE_FLOAT = 4
    HAPI_PARMTYPE_COLOR = 5
    HAPI_PARMTYPE_STRING = 6
    HAPI_PARMTYPE_PATH_FILE = 7
    HAPI_PARMTYPE_PATH_FILE_GEO = 8
    HAPI_PARMTYPE_PATH_FILE_IMAGE = 9
    HAPI_PARMTYPE_PATH_NODE = 10
    HAPI_PARMTYPE_FOLDERLIST = 11
    HAPI_PARMTYPE_FOLDER = 12
    HAPI_PARMTYPE_LABEL = 13
    HAPI_PARMTYPE_SEPARATOR = 14

    @staticmethod
    def load_parameters(engine, asset_name):

        wrapped = []
        parameters = engine.loadParameters(asset_name)

        for index in range(parameters.size()):
            parameter = HoudiniParameter(engine, asset_name, parameters.getParameter(index))

            if parameter.parentId >= 0:
                parent = next((parent for parent in filter(
                    lambda parent: parent.id == parameter.parentId, wrapped)), None)
                if parent:
                    parent.children.append(parameter)
                else:
                    raise HoudiniParameterException('Unable to find parent with id: %s' % parameter.parentId)
            else:
                wrapped.append(parameter)

        return wrapped

    def __init__(self, engine, asset_name, parameter=None):

        self.engine = engine
        self.asset_name = asset_name

        self.id = parameter.getId() if parameter else None
        self.parentId = parameter.getParentId() if parameter else None
        self.name = parameter.getName() if parameter else None
        self.label = parameter.getLabel() if parameter else None
        self.type = parameter.getType() if parameter else None
        self.size = parameter.getSize() if parameter else None

        self.children = []

    def get_value(self, index=0):

        if self.type == HoudiniParameter.HAPI_PARMTYPE_INT:
            return self.engine.getIntegerParameter(self.asset_name, self.id, index)

        elif self.type == HoudiniParameter.HAPI_PARMTYPE_FLOAT:
            return self.engine.getFloatParameter(self.asset_name, self.id, index)

        elif self.type == HoudiniParameter.HAPI_PARMTYPE_STRING:
            return self.engine.getStringParameter(self.asset_name, self.id, index)

        else:
            raise HoudiniParameterException('Unable to get value on unsupported parameter type: %s' % self.type)

    def set_value(self, value):

        if self.type == HoudiniParameter.HAPI_PARMTYPE_INT:
            self.engine.setIntegerParameter(self.asset_name, self.id, value)

        elif self.type == HoudiniParameter.HAPI_PARMTYPE_FLOAT:
            self.engine.setFloatParameter(self.asset_name, self.id, value)

        elif self.type == HoudiniParameter.HAPI_PARMTYPE_STRING:
            self.engine.setStringParameter(self.asset_name, self.id, value)

        else:
            raise HoudiniParameterException('Unable to set value on unsupported parameter type: %s' % self.type)


class HoudiniParameterException(Exception):
    pass


class HoudiniParameterControl(GenericControl):

    def __init__(self, id, parent, geometry_builder, ui_context):
        super(HoudiniParameterControl, self).__init__(id, parent, geometry_builder, ui_context)

        self.parameter = None
        self.increment = None

    def set_parameter(self, parameter):
        self.parameter = parameter

    def set_increment(self, increment):
        self.increment = increment

    def on_manipulate(self, position):
        if self.parameter and self.increment:
            direction = Direction.NEGATIVE if position.x <= self.position.x else Direction.POSITIVE
            new_value = self.parameter.get_value() + (self.increment * direction)

            self.parameter.set_value(new_value)     # TODO: add support for non-numeric values
