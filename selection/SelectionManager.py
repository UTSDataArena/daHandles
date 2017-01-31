from omega import *
from cyclops import *

from daHandles.cursor.controller.ControllerCursor import ControllerCursor
from daHandles.cursor.pointer.PointerCursor import PointerCursor


class SelectionManager(object):

    def __init__(self, ui_context):
        self.ui_context = ui_context

        self.nodes = []
        self.selections = {}
        self.intersection = None

    def add(self, node):
        self.nodes.append(node)

    def on_event(self):

        self.ui_context.on_event()

        for node in self.nodes:
            node.on_event()

        event = getEvent()

        if PointerCursor.is_interested(event):
            if event.isButtonDown(EventFlags.Button1):
                self.on_click(self.ui_context.pointer, getRayFromEvent(event))

        elif ControllerCursor.is_interested(event):
            cursor = self.ui_context.get_cursor(event)

            if isinstance(cursor, ControllerCursor) and event.isButtonDown(EventFlags.Button1):
                self.on_click(cursor, getRayFromPoint(int(cursor.get_position().x), int(cursor.get_position().y)))

    def on_click(self, cursor, ray):
        if ray[0]:
            querySceneRay(ray[1], ray[2], self.on_intersect, QueryFlags.QuerySort | QueryFlags.QueryFirst)

            event = getEvent()

            if self.intersection:
                self.on_select(cursor)
                event.setProcessed()

            elif cursor.id in self.selections and self.selections[cursor.id]:
                self.on_release(cursor)
                event.setProcessed()

            self.intersection = None

    def on_intersect(self, node, distance):
        if node:
            if not self.intersection:
                self.intersection = (node, distance)
            elif distance < self.intersection[1]:
                self.intersection = (node, distance)

    def on_select(self, cursor):
        context = next((context for context in filter(lambda context: context, map(lambda node: node.match(self.intersection[0]), self.nodes))), [])
        if context:
            if cursor.id in self.selections and self.selections[cursor.id] != context:
                self.on_release(cursor)

            self.selections[cursor.id] = list(context)

            node = context.pop()
            node.on_select(context)

    def on_release(self, cursor):
        if cursor.id in self.selections and self.selections[cursor.id]:
            context = list(self.selections[cursor.id])

            node = context.pop()
            node.on_release(context)

            self.selections[cursor.id] = None
