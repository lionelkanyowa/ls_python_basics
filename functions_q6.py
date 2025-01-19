# q6 Write a function that compares the length of two strings. it should return -1 if the first string 
# is shorter, 1 if the second string is shorter, and 0 if the're of equal length.

def compare_by_length(string1, string2):
    if len(string1) > len(string2):
        return 1
    elif len(string1) < len(string2):
        return -1
    else:
        return 0

print(compare_by_length('patience', 'perseverance'))
print(compare_by_length('strength', 'dignity'))
print(compare_by_length('humor', 'grace'))


