import json


class Registrations(dict):
    def __init__(self, people=None):
        super(Registrations, self).__init__(self)
        for person in people:
            self[people[person]['name']] = people[person]
