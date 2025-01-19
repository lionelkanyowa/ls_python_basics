# q5 Without running the following code, determine what it will print:

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

# multiples_of_three

# This will output the following:

# 3 / 1 = 3
# 6 / 2 = 3
# 9 / 3 = 3
# 12 / 4 = 3
# 15 / 5 = 3
# 18 / 6 = 3
# 21 / 7 = 3
# 24 / 8 = 3
# 27 / 9 = 3
# 30 / 10 = 3

multiples_of_three()