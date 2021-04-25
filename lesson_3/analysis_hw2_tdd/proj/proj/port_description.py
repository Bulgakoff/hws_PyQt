ATTR_NAME = "__port"


class Port:
    def __init__(self, default) -> None:
        self._validate_value(default)
        self._default = default
        self._name = None

    def __get__(self, instance, owner):
        return getattr(instance, self._name, self._default)

    def __set__(self, instance, value):
        self._validate_value(value)
        setattr(instance, self._name, value)
        # setattr(instance,self.default,value)

    def __set_name__(self, owner, name):
        self._name = f'__{name}'

    @staticmethod
    def _validate_value(val):
        if not isinstance(val, int):
            raise TypeError(f'It is not got int, got {type(val)}!')
        if not 0 < val <= 65365:
            raise ValueError('Invalid port value')
