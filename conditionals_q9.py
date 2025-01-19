# q.9 Without running the following code, determine wht will be printed.

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

# The code will output $3.99. Since the 'not' operator in line 4 is returning a falsy value 
# when it's operand is 'True'

