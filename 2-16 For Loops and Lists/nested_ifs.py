color = input('What color do you wear/are you? ')
if color == 'red':
    shell = input('do you have a shell as part of your body? ')
    if shell == 'yes':
        print('You are the red koopa.  Run!')
    else:
        print('You are Mario.')
elif color == 'green':
    human = input('Are you human?')
    if human == 'yes':
        print('You are Luigi, the lesser known brother, sorry')
    else:
        ridden = input('Are you rideable? ')
        if ridden == 'yes':
            print('You are Yoshi')
        else:
            print('You are a Green Koopa')
elif color == 'yellow':
    spikes = input('do you have spikes?')
    if spikes == 'yes':
        print('You are Bowser')
    else:
        print('You are Wario')
elif color == 'pink':
    print('You are Princess Peach')
elif color == 'blue':
    print('You are Rosalina')
elif color == 'purple':
    print('You are Waluigi? or maybe Wario if you\'re being sneaky.  ')
