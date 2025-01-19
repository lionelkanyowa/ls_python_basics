# q.7 Use Python's string methods on the string 'Captain Ruby' to create a string
# with the value 'Captain Python'

def string_transform(string):
    return string.replace('Ruby', 'Python')

print(string_transform('Captain Ruby'))

given_string = 'Captain Ruby'
replace_string = "Python"

def strip_change_string(string, replace_string):
    return(f'{given_string[0:given_string.index(' ')+1]}{replace_string}')

print(strip_change_string(given_string, replace_string))