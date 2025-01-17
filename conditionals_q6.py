# q.6 Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement
# Feel free to add more cases besides the 'sunny' and 'rainy'

weather = 'rainy'

match weather:
    case 'rainy':
        print('Grab your umbrella.')
    case 'sunny':
        print("Let's go outside.")
    case _:
        print('Stay Inside!')