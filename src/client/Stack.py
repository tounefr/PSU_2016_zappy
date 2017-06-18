
class Stack:
    def __init__(self, max_size = -1):
        self.items = []
        self.max_size = max_size

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def push(self, elem):
        if len(self.items) + 1 > self.max_size:
            raise RuntimeError("Stack size exceeded")
        self.items.insert(0, elem)