# q.7 What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# The code above will output 2. In line 6, the 'global' keyword was used to enable the global variable to be accessed
# by the local variable meaning that any operation on the local variable will affect the global variable, 
# when 'a' is now printed, it will output 2.

