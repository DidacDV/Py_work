class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size


    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError
        self._capacity = capacity


    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        self._size = size
