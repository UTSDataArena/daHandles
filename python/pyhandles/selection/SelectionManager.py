from omega import *
from cyclops import *

from pyhandles.cursor.controller.ControllerCursor import ControllerCursor
from pyhandles.cursor.pointer.PointerCursor import PointerCursor


class SelectionManager(object):

    def __init__(self, ui_context):
        self.ui_context = ui_context

        self.nodes = []
        self.selection = []
        self.intersection = None

    def add(self, node):
        self.nodes.append(node)

    def on_event(self):
        event = getEvent()

        if PointerCursor.is_interested(event):
            if event.isButtonDown(EventFlags.Button1):
                self.on_click(getRayFromEvent(event))

        elif ControllerCursor.is_interested(event):

            # todo: this will need further improvement to make sure we only respond to the cursor which owns the selection
            for cursor in self.ui_context.cursors:
                if isinstance(cursor, ControllerCursor) and event.isButtonDown(EventFlags.Button1):
                    self.on_click(getRayFromPoint(int(cursor.get_position().x), int(cursor.get_position().y)))

    def on_click(self, ray):
        if ray[0]:
            querySceneRay(ray[1], ray[2], self.on_intersect, QueryFlags.QuerySort | QueryFlags.QueryFirst)

            if self.intersection:
                self.on_select()
            elif self.selection:
                self.on_release()

            self.intersection = None

    def on_intersect(self, node, distance):
        if node:
            if not self.intersection:
                self.intersection = (node, distance)
            elif distance < self.intersection[1]:
                self.intersection = (node, distance)

    def on_select(self):
        context = next((context for context in filter(lambda context: context, map(lambda node: node.match(self.intersection[0]), self.nodes))), [])
        if context:
            if self.selection and self.selection != context:
                self.on_release()

            self.selection = list(context)

            node = context.pop()
            node.on_select(context)

    def on_release(self):
        if self.selection:
            context = list(self.selection)

            node = context.pop()
            node.on_release(context)

            self.selection = None
