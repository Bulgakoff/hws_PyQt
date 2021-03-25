class C:
    def __init__(self):
        self._x = "foo"

    @property
    def x(self):
        print("getter")
        return self._x

    @x.setter
    def x(self, value):
        print("setter")
        if value > 0:
            self._x = value
        else:
            self._x = 0

    @x.deleter
    def x(self):
        print("deleter")
        del self._x

    @property
    def hello(self):
        return f"hello {self._x}"


c = C()
print("c.hello", c.hello)

print("c.x", c.x)

c.x = -1
print("c.x", c.x)

del c.x
