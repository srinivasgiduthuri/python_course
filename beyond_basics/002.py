def operation(func, a, b):
    return func(a, b)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


print(operation(add, 10, 20))
print(operation(mul, 10, 20))
