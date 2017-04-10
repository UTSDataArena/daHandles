from daHandles.control.Control import Control


class ControlGroup(Control):

    def __init__(self, parent, ui_context):
        super(ControlGroup, self).__init__(parent, ui_context)

        self.controls = []

    def build(self):
        super(ControlGroup, self).build()

    def get_geo(self):
        return [control.get_geo() for control in self.controls]

    def set_visible(self, visible):
        for control in self.controls:
            control.set_visible(visible)

    def match(self, candidate):
        context = next((context for context in filter(lambda context: context, map(lambda control: control.match(candidate), self.controls))), [])
        if context:
            context.append(self)

        return context

    def prepare(self, selector, selection, context):
        for control in self.controls:
            if control.is_selected and control != selection:
                control.on_release(selector, context)

    def on_select(self, selector, context):
        super(ControlGroup, self).on_select(selector, context)

        control = context.pop()
        if control:
            self.prepare(selector, control, context)
            control.on_select(selector, context)

    def on_release(self, selector, context):
        super(ControlGroup, self).on_release(selector, context)

        control = context.pop()
        if control:
            self.prepare(selector, control, context)
            control.on_release(selector, context)

    def on_event(self, event):
        for control in self.controls:
            control.on_event(event)

    def on_manipulate(self, control, origin, movement):
        raise NotImplementedError
