# Examine the code shown below. Without running it, determine what it will print. If you're not sure,
#refer to the Python book

animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

# The following code will print 'neigh'

