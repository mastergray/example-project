# An example of some "functional programming" in Python:

# adder :: NUMBER -> NUMBER -> NUMBER
# Returns a curried function that subtracts the first argument from the second:
def adder(x):
    return lambda y : x + y

# subber :: NUMBER -> NUMBER -> NUMBER
# Returns a curried function that subtracts the first argument from the second:
def subber(x):
    return lambda y : x - y

# fold ::  (b -> a -> b) -> b -> [a] -> b
# Transfroms a list of values into a single value: 
def fold(fn, arr, acc):
    return  acc if len(arr) == 0 else fold(fn, arr[1:len(arr)], acc=fn(acc, arr[0]))


# map :: (a -> b), [a] -> [b]
# Transform a list of values into some other list of values
def map(fn, arr):
    return fold(lambda x, y : x + [fn(y)], arr, [])

# filter :: (a -> BOOLEAN), [a] -> [a]
# Returns only the elements for an array that are TRUE for the given function:
def filter(fn, arr):
    return fold(lambda x,y : x + [y] if fn(y) == True else x, arr, [])

# compose :: (b -> c) -> (a -> b) -> (a -> c)
# Applies the result of a unary function as the argument to another unary function:
def compose(a, b):
    return lambda x : b(a(x))

# composeAll :: [(a -> a)] -> (a -> a)
# Transforms an array of unary functions into a single unary function:
def composeAll(fns):
    return fold(lambda x,y : compose(x,y), fns, (lambda z : z))

# logger :: VOID -> a -> a
# Returns function that prints a value and then returns it:
def logger():
    return lambda x : [print(x), x][1]

# This gets executed if we run the module directly - otherwise this is ignored when imported by another script:
if (__name__ == '__main__'):
 
    listOfAdders = composeAll([
        adder(2),
        adder(4),
        adder(6),
        adder(8),
        logger()
    ])

    listOfAdders(10) # Prints "30"

    printAdder = lambda x : composeAll([
        adder(x), logger()
    ])

    add5 = printAdder(5)
    add5(10); # Print 15
