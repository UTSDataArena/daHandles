class SelectionContext(object):

    def __init__(self, selector=None, selection=None):
        super(SelectionContext, self).__init__()

        self.selector = selector
        self.selection = [] if not selection else selection

    def pop(self):
        return self.selection.pop()
