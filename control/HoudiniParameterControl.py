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

        parameters_by_name = {}
        parameters = engine.loadParameters(asset_name)

        for index in range(parameters.size()):
            parameter = HoudiniParameter(engine, asset_name, parameters.getParameter(index))

            if parameter.parentId >= 0:
                parent = next((parent for parent in filter(
                    lambda parent: parent.id == parameter.parentId, parameters_by_name.values())), None)
                if parent:
                    parent.children.append(parameter)
                else:
                    raise HoudiniParameterException('Unable to find parent with id: %s' % parameter.parentId)
            else:
                parameters_by_name[parameter.name] = parameter

        return parameters_by_name

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
            return self.engine.getIntegerParameterValue(self.asset_name, self.id, index)

        elif self.type == HoudiniParameter.HAPI_PARMTYPE_FLOAT:
            return self.engine.getFloatParameterValue(self.asset_name, self.id, index)

        elif self.type == HoudiniParameter.HAPI_PARMTYPE_STRING:
            return self.engine.getStringParameterValue(self.asset_name, self.id, index)

        else:
            raise HoudiniParameterException('Unable to get value on unsupported parameter type: %s' % self.type)

    def set_value(self, value, index=0):

        if self.type == HoudiniParameter.HAPI_PARMTYPE_INT:
            self.engine.setIntegerParameterValue(self.asset_name, self.id, index, int(value))

        elif self.type == HoudiniParameter.HAPI_PARMTYPE_FLOAT:
            self.engine.setFloatParameterValue(self.asset_name, self.id, index, float(value))

        elif self.type == HoudiniParameter.HAPI_PARMTYPE_STRING:
            self.engine.setStringParameterValue(self.asset_name, self.id, index, str(value))

        else:
            raise HoudiniParameterException('Unable to set value on unsupported parameter type: %s' % self.type)


class HoudiniParameterException(Exception):
    pass


class HoudiniParameterControl(GenericControl):

    def __init__(self, id, parent, geometry_builder, ui_context):
        super(HoudiniParameterControl, self).__init__(id, parent, geometry_builder, ui_context)

        self.parameter = None
        self.value_index = None
        self.increment = None
        self.rate_limiter = None
        self.min_value = None
        self.max_value = None

    def set_parameter(self, parameter):
        self.parameter = parameter

    def set_value_index(self, value_index):
        self.value_index = value_index

    def set_increment(self, increment):
        self.increment = increment

    def set_rate_limiter(self, rate_limiter):
        self.rate_limiter = rate_limiter

    def set_min_value(self, min_value):
        self.min_value = min_value

    def set_max_value(self, max_value):
        self.max_value = max_value

    def on_manipulate(self, position):

        if self.parameter and self.increment:

            if self.parameter.type == HoudiniParameter.HAPI_PARMTYPE_STRING:
                raise NotImplementedError   # TODO: add support for non-numeric values
            else:
                if self.rate_limiter and not self.rate_limiter.is_active():     # TODO: what if no rate limiter is specified?

                    self.parent.on_manipulate(self, self.position, position)
                    self.set_position(position)
