# -*- coding: utf-8 -*-
class Municipio:
    def __init__(self, name, history, inhabitants, affiliates, events,coordinador):
        self.name = name
        self.history = history
        self.inhabitants = inhabitants
        self.affiliates = affiliates
        self.events = events
        self.coordinador = coordinador


    def add_event(self, event_name):
        self.events.append(event_name)

    def remove_event(self, event_name):
        if event_name in self.events:
            self.events.remove(event_name)

