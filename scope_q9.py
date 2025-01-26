# q.9 What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# The code will output 7. `The print()` function in line 9 is still pointing to the global variable
# a.   
# In Python, integers are immutable, meaning their values cannot be changed.