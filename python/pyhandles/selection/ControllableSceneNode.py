from pyhandles.selection.SelectableSceneNode import SelectableSceneNode


class ControllableSceneNode(SelectableSceneNode):

    def __init__(self, name, geo=None):
        super(ControllableSceneNode, self).__init__(name, geo)

        self.controls = []

    def match(self, candidate):
        context = super(ControllableSceneNode, self).match(candidate)
        if not context:
            context = next((context for context in filter(lambda context: context, map(lambda control: control.match(candidate), self.controls))), [])
            if context:
                context.append(self)

        return context

    def on_select(self, context):
        if not self.is_selected:
            self.show_controls()
            super(ControllableSceneNode, self).on_select(context)

        if context:
            control = context.pop()
            control.on_select(context)

    def on_release(self, context):
        if self.is_selected:
            if context:
                control = context.pop()
                control.on_release(context)

            self.hide_controls()
            super(ControllableSceneNode, self).on_release(context)

    def add_control(self, control):
        self.controls.append(control)
        for geo in control.get_geo():
            self.node.addChild(geo)

    def show_controls(self):
        for control in self.controls:
            control.set_visible(True)

    def hide_controls(self):
        for control in self.controls:
            control.set_visible(False)
