# q.2 What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# This will likely print an error since the x in the global scope is not the same x
# within the local scope. since x has not yet been initialized in the local scope, it has nothing to
# reference to therefore will output an error.