import jinja2
import json
import re

import kolala.framework.aiml as aiml
import kolala.game.Items


class ChatResponder(object):
    def __init__(self):
        self.engine = aiml.Kernel()
        self.engine.verbose()

        self.engine.learn("kolala/framework/aiml/aiml/*.aiml")

    def respond(self, message, session=None):
        if session is None:
            response = self.engine.respond(message)
        else:
            response = self.engine.respond(message, session)
        response = ChatResponder.template(response)
        return response

    @staticmethod
    def search(match):
        print("Searching: " + match)
        things = kolala.game.Items.items.find(match)
        found = []
        for thing in things:
            i = {}
            i["name"] = thing["name"]
            found.append(i)
        return found

    @staticmethod
    def template(message):
        needle = '\[\[([^\]]+)\]\]'
        expanded = message
        result = re.match(needle, message)
        search = []
        package = {}
        if result:
            search = ChatResponder.search(result.groups()[0])
            expanded = re.sub(needle, '', message, 1)
        package["search"] = search
        tmp = jinja2.Template(expanded)
        expanded = tmp.render(package)
        return expanded
