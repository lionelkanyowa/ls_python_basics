# q.10 Determine what the following code snippet prints. First solve it in your head or on 
# paper, then run it in your Python environment to check the result.

speed = 0
acceleration = 24
breaking_force = 19
is_moving = breaking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# True and (False or True)
# True and True
# True (Final answer)
# the code above will print 'True' based on the above analysis.

# **Bonus question** Do we need parenthesis in the boolean expression or could we have written 
# the following?

is_moving = breaking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)

# Yes parenthesis are needed since 'and' has a higher order precedence than 'or' 

