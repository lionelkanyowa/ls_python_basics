# q.4 What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)

my_function()

# My attempt at answering the question. (Wrong answer)
# The code above will not print anything and likely output an error. In line 5 we have a function that uses the 
# print() function to output the variable 'a'. However, with scoping rules variables within a local scope are not 
# accessible to the global scope, so print(a) has nothing to reference to since it wasn't initialized within the 
# function.

# Right answer after running the code
# After running the code, the code actually output '1'. This is due to variable shadowing. The variable 'a' 
# initialized in line 3 is globally accessible throughout the code, meaning it can be accessed within the function
# which is why when the function is called, the output will be '1'
