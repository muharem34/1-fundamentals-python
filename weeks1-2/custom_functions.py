def myFn():
    print("You have called a function")


myFn()


def add(x, y):
    z = x + y
    print(z)


add(2, 3)
add(6, 7)


# def add(x,y):
#     return x + y
#     print(add(3,4))

# statement after Return will not be executed
def myfunction():
    return 3+3
    print("Hello, World!")


print(myfunction())


def a_function(callback):
    print(callback(3))


a_function(lambda num: num ** 2)
