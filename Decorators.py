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


#########################
# functions in python are objects which means we can pass them around
# args and kwargs will accept all args passed in

def func(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print('i am func')

    return wrapper


@func
def func2(x, y):
    print(x, y)


@func
def func3():
    print('i am func3')


# we just want to call function2 and decorator. rather than
# call func and pass func2, we can @func

func2(5, 6)
func3()
# x = func(func2)
# print(x.__name__)
# x()
# x = func(func3)
# print(x.__name__)
# x()


#########################

def func(f):
    def wrapper(*args, **kwargs):
        re = f(*args, **kwargs)
        print('i am func')
        return re
    return wrapper


@func
def func2(x, y):
    print(x)
    return y


@func
def func3():
    print('i am func3')


# we just want to call function2 and decorator. rather than
# call func and pass func2, we can @func

print(func2(5, 6))

func3()
