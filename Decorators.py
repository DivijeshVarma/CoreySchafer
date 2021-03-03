# Decorators allow us to modify behaviour of function without
# changing any of its code
# Decorators is callable function object which will take a function
# and modify it, it will return that function
# --Need to take a function as a parameter
# --Add functionality to function
# --Function need to return another function


def outer(func):

    def inner():
        var = func()
        return var.title()

    return inner


@outer
def print_str():
    return 'divijesh'


print(print_str())
