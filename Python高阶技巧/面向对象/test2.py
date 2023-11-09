import random

var_1: int = 12
var_2 = random.randint(1, 10)  # type: int


def func(data: list) -> list:
    data.append(2)
    return data


class imp:
    def make(self):
        pass

print(func([]))
print(var_1)
print(var_2)
