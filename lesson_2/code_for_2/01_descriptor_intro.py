# --------------------- Дескрипторы атрибутов -------------------------------

print(" ========== Базовый пример работы с дескриптором атрибутов ===========")


class TypedProperty:
    def __init__(self, name, type_name, default=None):
        print("__init__")
        self.name = "_" + name
        self.type = type_name
        self.default = default if default else type_name()

    def __get__(self, instance, cls):
        print("__get__")
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        print("__set__")
        if not isinstance(value, self.type):
            raise TypeError("Значение должно быть типа %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        print("__delete__")
        raise AttributeError("Невозможно удалить атрибут")


class Foo:
    name = TypedProperty("name", str)
    # num = TypedProperty("num", int, 42)


if __name__ == "__main__":
    f = Foo()
    b = Foo()
    a = f.name  # Неявно вызовет Foo.name.__get__(f, Foo)
    f.name = "Гвидо"  # Вызовет Foo.name.__set__(f, "Guido")
    f.name = 4
    del f.name  # Вызовет Foo.name.__delete__(f)
