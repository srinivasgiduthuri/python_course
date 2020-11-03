def log(func):
    def wrapper_function():
        print("Pre-process")
        func()
        print("Post-process")

    return wrapper_function


@log
def hello():
    print("Hello Python")


hello()
