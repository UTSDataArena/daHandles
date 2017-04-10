from daHandles.selection.SelectableSceneNode import SelectableSceneNode


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

    def on_select(self, selector, context):
        if not self.is_selected:
            self.show_controls()
            super(ControllableSceneNode, self).on_select(selector, context)

        if context and selector == self.selector:
            control = context.pop()
            control.on_select(selector, context)

    def on_release(self, selector, context):
        if self.is_selected and selector == self.selector:
            if context:
                control = context.pop()
                control.on_release(selector, context)

            self.hide_controls()
            super(ControllableSceneNode, self).on_release(selector, context)

    def on_event(self, event):
        for control in self.controls:
            control.on_event(event)

    def add_control(self, control):
        self.controls.append(control)
        for geo in control.get_geo():
            self.node.addChild(geo)

    def show_controls(self):
        for control in self.controls:
            control.show()

    def hide_controls(self):
        for control in self.controls:
            control.hide()
