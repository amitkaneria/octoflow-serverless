from typing import Any


class Validator:
    type_check = None

    def __init__(self, type: Any = None):
        self.type_check = type

    def validate(self, value):
        return isinstance(value, self.type_check)


mapper= {
    "int": Validator(int),
    "float": Validator(float),
}

data = {}