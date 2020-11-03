def func1(x, y):
    print("Function 1")


def func2(name, email):
    print("Function 2")


def call_func(func, *args, **kwargs):
    func(*args, **kwargs)


# 10, 20 will be in *args
call_func(func1, 10, 20)

# name and email in **kwargs
call_func(func2, name='Abc', email='abc@abc.com')
