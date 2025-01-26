# q3 What will the following code do and why? Don't run it until you have tried to answer.

def my_function():
    a = 1

    if True:
        print(a)

my_function()

# This will output '1', the if statement block in line 6 has a print function to output the variable 'a'
# That variable is still accessible within the function and is still within scope, 
# hence we get the output of 1 when the function is called.
#  