def square(x):
    return x * x


f1 = square(5)
# we assigned function to variable
f = square
print(f)
print(f(5))
print(f1)

# we can pass functions as arguments and returns function
# as result of other functions

# if function accepts other functions as arguments or
# return functions as a result i.e higher order function
# adding paranthesis will execute function.
# # we can pass functions as arguments:--


def square(x):
    return x * x


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4])
print(squares)


# to return a function from another function, one of the
# aspects for first class function
# log variable is equal to log_message function, so we can
# run log variable as just like function, it remembers
# message from logger function

def logger(msg):

    def log_message():
        print(f"log: {msg}")

    return log_message


log = logger('hi')
log()


# it remembers tag we passed earlier

def html_tag(tag):

    def wrap_text(msg):
        print(f"<{tag}>{msg}<{tag}>")

    return wrap_text


p_h1 = html_tag('h1')
p_h1('Test headline')
p_h1('Another headline')

p_p1 = html_tag('p1')
p_p1('Test paragraph')
