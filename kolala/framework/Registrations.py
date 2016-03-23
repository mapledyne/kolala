import hashlib
import json
import os

from kolala.Config import config
import kolala.framework.Utils as utils


class Registrations(dict):
    def __init__(self):
        super(Registrations, self).__init__(self)
        self.file = config['home_path'] + 'registrations.json'
        self._load_people()

    def _load_people(self):
        if not os.path.isfile(self.file):
            return
        with open(self.file, 'r') as openfile:
            text = openfile.read()
        people = json.loads(text)
        for person in people:
            self[person] = people[person]

    def save(self):
        with open(self.file, 'w+') as writefile:
            writefile.write(json.dumps(self, indent=4))

    def register(self, user, password):
        self[user] = {'password': utils.md5hash(password)}
        self.save()
