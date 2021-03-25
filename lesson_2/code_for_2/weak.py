class Foo:
    pass


a = Foo()
b = a
print(a is b)

c = Foo()
print(a is c)
