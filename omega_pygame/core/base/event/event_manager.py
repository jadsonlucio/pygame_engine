import pygame
from .event import Event
from .custom_events import *


class Events:
    def __init__(self, widget):
        self.widget = widget
        self.events = [
            # mouse events
            Event(widget, "mouse_down", pygame.MOUSEBUTTONDOWN, self.widget.mouse_down, self.mouse_down_val),
            Event(widget, "mouse_up", pygame.MOUSEBUTTONUP, self.widget.mouse_up, self.mouse_up_val),
            Event(widget, "mouse_motion", pygame.MOUSEMOTION, self.widget.mouse_moved, self.mouse_moved_val),
            Event(widget, "mouse_clicked", MOUSECLICKED, self.widget.mouse_clicked, self.mouse_clicked_val),
            Event(widget, "mouse_hold", MOUSEHOLD, self.widget.mouse_hold, self.mouse_hold_val),
            Event(widget, "mouse_in", MOUSE_IN, self.widget.mouse_in, self.mouse_in_val),
            Event(widget, "mouse_out", MOUSE_OUT, self.widget.mouse_out, self.mouse_out_val),
            Event(widget, "mouse_over", MOUSE_OVER, self.widget.mouse_over, self.mouse_over_val),

            # keyboard events
            Event(widget, "key_up", pygame.KEYUP, self.widget.key_up, self.key_up_val),
            Event(widget, "key_down", pygame.KEYDOWN, self.widget.key_down, self.key_down_val),
            Event(widget, "key_hold", KEYHOLD, self.widget.key_hold, self.key_hold_val),
            Event(widget, "key_pressed", KEYPRESSED, self.widget.key_pressed, self.key_pressed_val),

            # window events
            Event(widget, "window_resize", pygame.VIDEORESIZE, self.widget.window_resize, self.window_resize_val)
        ]

        self.dict_events_name = {}
        self.dict_events_key = {}

        for event in self.events:
            self.dict_events_name[event.name] = event
            self.dict_events_key[event.key] = event

        self._on_events = []

    def bind(self, event_name, callback):
        if event_name in self.dict_events_name:
            event = self.dict_events_name[event_name]
            event.bind(callback)
        else:
            raise Exception(f"event of name {event_name} don't exist")

    def process_events(self, events):
        custom_events = get_widget_custom_event(self.widget)
        allowed_events = []

        for event in events + custom_events:
            if event.type in self.dict_events_key:
                event = self.dict_events_key[event.type].update(event)
            else:
                event = self.widget.on_event(event)

            if event is not None:
                allowed_events.append(event)

        return allowed_events

    def window_resize_val(self, event):
        return event

    def mouse_over_val(self, event):
        if self.widget.is_mouse_over:
            return event

    def mouse_in_val(self, event):
        return event

    def mouse_out_val(self, event):
        return event

    def mouse_up_val(self, event):
        if self.widget.mouse_on:
            return event

    def mouse_down_val(self, event):
        if self.widget.mouse_on:
            return event

    def mouse_clicked_val(self, event):
        if self.widget.mouse_on:
            return event

    def mouse_moved_val(self, event):
        if self.widget.mouse_on:
            return event

    def mouse_hold_val(self, event):
        if self.widget.mouse_on:
            return event

    def key_pressed_val(self, event):
        return event

    def key_hold_val(self, event):
        return event

    def key_up_val(self, event):
        return event

    def key_down_val(self, event):
        return event

    def on_event(self, event):
        return event
