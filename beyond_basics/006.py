def log(func):
    def decorator_function(*args, **kwargs):
        print('Calling ', func.__name__)
        print('Arguments :', args, kwargs)
        func(*args, **kwargs)
        print('Completed', func.__name__)

    return decorator_function


@log
def hello(name):
    print('Hello', name)


@log
def add(a, b):
    print(a + b)


hello('Decorators')  # Call function that is decorated
hello(name='Decorators')
add(10, 20)  # Call function that is decorated and called with *args
add(a=10, b=20)  # Call function that is decorated and called with **kwargs
