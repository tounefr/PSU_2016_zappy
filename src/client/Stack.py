
class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop(0)

    def push(self, elem):
        self.items.insert(0, elem)