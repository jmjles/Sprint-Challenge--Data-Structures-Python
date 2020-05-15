class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.pointer = 0

    def append(self, item):
        self.storage[self.pointer] = item
        self.pointer += 1

        if self.pointer == self.capacity:
            self.pointer = 0
        
    def get(self):
        storage = self.storage
        return [item for item in storage if item is not None ]
