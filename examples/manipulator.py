import math
from cyclops import *

from daHandles.context.UiContext import UiContext
from daHandles.control.CustomControlGeometryBuilder import CustomControlGeometryBuilder
from daHandles.control.TransformControlGroupBuilder import TransformControlGroupBuilder
from daHandles.control.WhiskerControlBuilder import WhiskerControlBuilder
from daHandles.cursor.controller.SpaceNavControllerCursor import SpaceNavControllerCursor
from daHandles.selection.ControllableSceneNode import ControllableSceneNode
from daHandles.selection.SelectionManager import SelectionManager


if __name__ == '__main__':
    """
    This example demonstrates how to setup a scene containing objects which may
    be manipulated using on-screen handles.   It show show to use many of the
    features which are provided by the daHandles library, including:

        - How to specify controllers and add them to the UI context
        - How to use builders to create control geometry, controls and control groups
        - How to specify scene nodes and attach controls to them
        - How to set up a selection manager to process user interactions via controls
    """

    ui_context = UiContext()
    ui_context.add_cursor(SpaceNavControllerCursor('spacenav', '/da/sw/omegalib/myCursor.png', ui_context))

    getDefaultCamera().setControllerEnabled(False)

    geo1 = BoxShape.create(1, 1, 1)
    geo1.setEffect('colored -d white')
    bbox1 = (geo1.getBoundMinimum(), geo1.getBoundMaximum())

    geometry_builder = CustomControlGeometryBuilder()
    geometry_builder.set_name('handle')
    geometry_builder.set_path('/da/dev/luke/sources/daHandles/resources/handle.obj')

    control_builder = WhiskerControlBuilder()
    control_builder.set_geometry_builder(geometry_builder)

    transform_builder = TransformControlGroupBuilder()
    transform_builder.set_ui_context(ui_context)
    transform_builder.set_control_builder(control_builder)

    box1 = ControllableSceneNode('box1', geo1)
    box1.add_control(transform_builder.set_parent(box1).set_bounding_box(bbox1).build())
    box1.node.setPosition(Vector3(-1.5, 1.5, -10))
    box1.node.rotate(Vector3(0, 1, 0), math.radians(-45), Space.Local)

    geo2 = BoxShape.create(1, 1, 1)
    geo2.setEffect('colored -d white')
    bbox2 = (geo2.getBoundMinimum(), geo2.getBoundMaximum())

    box2 = ControllableSceneNode('box2', geo2)
    box2.add_control(transform_builder.set_parent(box2).set_bounding_box(bbox2).build())
    box2.node.setPosition(Vector3(1.5, 1.5, -10))
    box2.node.rotate(Vector3(0, 1, 0), math.radians(-45), Space.Local)

    light = Light.create()
    light.setEnabled(True)
    light.setPosition(Vector3(0, 5, -2))
    light.setColor(Color(1.0, 1.0, 1.0, 1.0))
    light.setAmbient(Color(0.1, 0.1, 0.1, 1.0))

    manager = SelectionManager(ui_context)
    manager.add(box1)
    manager.add(box2)

    setEventFunction(manager.on_event)