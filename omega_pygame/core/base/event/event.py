class Event:
    def __init__(self, widget, name, key, callback=None, validator=None):
        self.widget = widget
        self.name = name
        self.key = key
        self.callback = callback
        self.validator = validator
        self.binds = []
        self.event_obj = None

    def bind(self, bind_func):
        self.binds.append(bind_func)

    def update(self, event):
        if self.validator is not None:
            event = self.validator(event)

        if event is not None:
            self.event_obj = event
            for bind_func in self.binds:
                bind_func(self.widget, event)

            event = self.callback(event)

        return event
