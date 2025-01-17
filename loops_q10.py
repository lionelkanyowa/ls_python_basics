# q.10 Modify the following code so the loop continues iterating until the user inputs 'yes'

while True:
    print('Should i stop looping?')
    answer = input()
    if answer == 'yes':
        break
    print("Enter 'yes' to exit" )
