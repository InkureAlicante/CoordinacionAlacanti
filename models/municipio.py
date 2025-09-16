# -*- coding: utf-8 -*-
class Municipio:
    def __init__(self, name, history, inhabitants, affiliates, events, info_tables, coordinador, LISTA, team_members):
        self.name = name
        self.history = history
        self.inhabitants = inhabitants
        self.affiliates = affiliates
        self.events = events
        self.info_tables = info_tables
        self.coordinador = coordinador
        self.LISTA = LISTA
        self.team_members = team_members

    def add_event(self, event_name):
        self.events.append(event_name)

    def remove_event(self, event_name):
        if event_name in self.events:
            self.events.remove(event_name)

