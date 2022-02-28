if False:
    a_list = [1, 2, 3, 4, 5]
    print(a_list)
    a_list.remove(3)
    print(a_list)
    """
        Remove removes by value not by index
        
            it only removes one value, the first one that is found
    """

    b_list = [1, 2, 3, 4, 5, 4, 3, 3, 4, 5, 3, 3]
    b_list.remove(3)
    b_list.remove(3)
    b_list.remove(3)
    print(b_list)

    zero_instances = [1, 4, 4, 2, 6, 2, 7, 8]
    if 3 in zero_instances:
        print('removing element')
        zero_instances.remove(3)
    else:
        print('no element found')

    """
    test_list = [1, 5, 2, 4, 8, 5, 6, 6, 8, 3, 4, 5, 1]
    for x in test_list:
        print(test_list)
        if x % 2 == 1:
            test_list.remove(x)
            
    test_list = [1, 5, 2, 4, 8, 5, 6, 6, 8, 3, 4, 5, 1]
    for i in range(len(test_list)):
        print(test_list)
        if test_list[i] % 2 == 1:
            test_list.remove(test_list[i])
    
    
    print(test_list)
    """

    test_list = [1, 5, 2, 4, 8, 5, 6, 6, 8, 3, 4, 5, 1]

    new_list = []

    for x in test_list:
        if x % 2 == 0:
            new_list.append(x)

    print(new_list)

    test_list = [1, 5, 2, 4, 8, 5, 6, 6, 8, 3, 4, 5, 1]
    removed = 0
    for i in range(len(test_list)):
        print(test_list)
        if test_list[i - removed] % 2 == 1:
            test_list.remove(test_list[i - removed])
            removed += 1

    print(test_list)

    """
        While loops are a different sort of thing
            While loops are if statements on repeat
            
         - Think: Whenever I don't know how many times the loop will run, use while.
            If I do know, its the length of a list, or maybe its just 10 , or for some reason it's input value
            then I know.  
    """

    user_input = input('...> ')
    while user_input != 'quit':
        user_input = input('...> ')

    my_favorite_list = [1, 5, 4, 7, 9, 8, 2]
    index = 0
    while index < len(my_favorite_list):
        print(my_favorite_list[index])
        # most common way to make an infinite loop is to just forget to update your index variable
        # string variable
        index += 1
        # very important must have index += 1 or else infinite loop

    """
    board = [[], []]
    
    while not checkmate(board):
        # play game
        pass
    """

    x = 1
    count = 0
    the_number = int(input('Tell me a number: '))
    while x < the_number:
        count += 1
        x *= 2
        # x = x * 2
    print(f'{the_number} is less than {x} and the count is {count}')
    """
        count is calculating a logarithm of the_number
    """

    favorite_foods = []
    # prime the input
    food = input('What is one of your favorite foods? ')
    while food != 'quit':
        favorite_foods.append(food)
        # more code in here
        # last thing you do should be to get the next input
        food = input('What is one of your favorite foods? ')

    print(favorite_foods)

    bad_list = [1, 4, 3, 6, 3, 5, 6, 8, 8, 6, 3, 6, 6, 3, 3, 3, 3, 8, 9, 4]
    while 3 in bad_list:
        print(bad_list)
        bad_list.remove(3)

    print(bad_list)


number = 1
while number < 100:
    print(number)
    number += 2

for number in range(1, 100, 2):
    print(number)

"""
    Any for loop can be recoded as a while loop.
    
        While loops are more general purpose than for loops.
        
    Not all while loops can be recoded as for loops.  
"""

"""
    GUI programs, server code
        giant while loops...
"""

guess_number = int(input('What number should people guess? '))

turn_count = 1
guess = guess_number + 1

while guess != guess_number:
    if turn_count % 2 == 1:
        guess = int(input('Player 1, it is your turn, what is your guess? '))
    else:
        guess = int(input('Player 2, it is your turn, what is your guess? '))

    turn_count += 1

print(turn_count)
if (turn_count + 1) % 2 == 0:
    print('Player 2 won')
else:
    print('Player 1 won')
