# q.9 Loop over the elements of the 'fish_list' list below, logging each one. terminate the
# loop immediately after printing the string 'Nemo'

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

index = 0
while index < len(fish_list):
    print(fish_list[index])
    
    if fish_list[index] == 'Nemo':
        break
    index += 1


for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

    
