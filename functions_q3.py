# q.3 Let's generalize the function from the previous exercise. Implement a function named 
# cite that takes two string arguments: the author of the quote and what they said. 
# It then prints the quote, as shown below.

def cite(string1, string2):
    print(f'{string1} said: "{string2}"')

cite('Bruce Eckel', 'Python is executable pseudocode')