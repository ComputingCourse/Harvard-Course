class Jar:
    def __init__(self, capacity= 12):
        self.capacity = str(capacity)
        self.num_cookies = 0

    def __str__(self):
        string = ""
        for i in range(self.num_cookies):
            string += "🍪"
        return string

    def deposit(self, n):
        self.num_cookies+=int(n)
        if self.num_cookies > self.capacity:
            raise ValueError("Too many")

    def withdraw(self, n):
        self.num_cookies-=int(n)
        if self.num_cookies < 0:
            raise ValueError("Too many")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity.isnumeric():
            if int(capacity) > 0:
                self._capacity = int(capacity)
            else:
                raise ValueError("Incorrect")
        else:
            raise ValueError("Incorrect")


    @property
    def size(self):
        return self.num_cookies

