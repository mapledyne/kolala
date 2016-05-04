
class Friend(dict):
    pass


class Friends(dict):
    def add(self, name, bits):
        if name not in self.keys:
            self[name] = Friend(bits)
        else:
            raise KeyError
