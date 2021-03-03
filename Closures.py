# inner fun access the msg variable its called
# free cariable, because its not defined in inner fun
# but still have access to inner_fun function

def outer_fun():
    msg = 'hi'

    def inner_fun():
        print(msg)

    return inner_fun()


outer_fun()


# instead of executing inner_fun it returns function to
# my_fun variable and it is equal to inner_fun function
# wer'e done with execution of outer_fun but inner_fun we
# returned still have access to msg variable that's called
# closure and closure is inner function that remembers and
# has access to variables to local scope in which it is
# created even outer_fun finished executing.

def outer_fun():
    msg = 'hi'

    def inner_fun():
        print(msg)

    return inner_fun


my_fun = outer_fun()
print(my_fun.__name__)

my_fun()


###############

def outer_fun(ms):
    msg = ms

    def inner_fun():
        print(msg)

    return inner_fun


hi_fun = outer_fun('hi')
hello_fun = outer_fun('hello')

hi_fun()
hello_fun()
