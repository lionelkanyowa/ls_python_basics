# q.5 What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# My Answer (Wrong answer)
# The code will output 1. This is because when the function calls itself in line 8, it starts by printing out
# the variable 'a', and since print(a) is executed before 'a' is reassigned in line 7, variable 'a' in line
# will still be referencing to the global variable in line 3, hence the output will be '1'. 

# Correct answer
# The code will raise an error. Python detects that 'a' is being assigned within the 'my_function' function and treats
# 'a' as a local variable. And since we trying to print the local 'a' before it has been assigned, it will output an 
# error.