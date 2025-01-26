# q.6 What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)

# The code above will output 1. The print function in line 9 is referencing the global variable in line 3.
# Within the function, the local variable 'a' has no affect on the global variable.
# 
#   
    