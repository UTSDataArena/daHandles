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

    def prepare(self, selection, context):
        for control in self.controls:
            if control.is_selected and control != selection:
                control.on_release(context)

    def on_select(self, context):
        super(ControlGroup, self).on_select(context)

        control = context.pop()
        if control:
            self.prepare(control, context)
            control.on_select(context)

    def on_release(self, context):
        super(ControlGroup, self).on_release(context)

        control = context.pop()
        if control:
            self.prepare(control, context)
            control.on_release(context)

    def on_manipulate(self, control, origin, movement):
        raise NotImplementedError
