# q.7 Predict the output of the following code:

if False or True:
    print('Yes')
else:
    print('No...')

# My answer:
# This will print 'Yes' because the logical operator `or` evaluates both conditions `False` and `True`
# before short circuiting and since one condition needs to be true with an `or` operator, the `if/else` 
# returns a 'truthy' value. 

# Launch School's answer:
# The condition provided to our if statement uses the logical or operator, or. Therefore, the condition 
# evaluates to a truthy value if either of its operands is truthy. Since True is truthy, 
# the condition always evaluates as truthy.