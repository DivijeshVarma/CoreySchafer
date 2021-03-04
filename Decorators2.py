# first class functions allow us to treat functions like any other
# object, for example we can pass functions as arguments to another
# function, we can return functions and we can assign functions to
# variable. Closures-- it will take advantage of first class functions
# and return inner function that remembers and has access to variables
# local to scope in which they were created.


def outer_func(mg):
    def inner_func():
        print(mg)
    return inner_func


hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()


# Decorator is function that takes another function as an argument
# add some functionality and returns another function, all of this
# without altering source code of original function you passed in.
# Decorating our functions allow us to easily add functionality to
# our existing functions, by adding functionality inside wrapper
# without modifying original display function in any way and add
# code in wrapper in any way

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print(f"wrapper function executed {original_func.__name__}")
        original_func(*args, **kwargs)
    return wrapper_func


@decorator_func
def display():
    print('display function')


@decorator_func
def display_info(name, age):
    print(f"name:{name}, age:{age}")


display()
display_info('divi', 27)


print('--------------------------------')


##################################
class decorator_class(object):

    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print(f"call method executed {self.original_func.__name__}")
        return self.original_func(*args, **kwargs)


@decorator_class
def display():
    print('display function')


@decorator_class
def display_info(name, age):
    print(f"name:{name}, age:{age}")


display()
display_info('divi', 27)
