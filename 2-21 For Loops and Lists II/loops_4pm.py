"""
    what is a list?
        a list is a ordered collection of elements.
        0th, 1st, 2nd, ...

        to access elements in a list you use index
        0 <= index < len(list)
"""
if False:
    my_words = ['apple', 'bear', 'car', 'dent', 'effort']
    print(my_words[2])

    """
    for each loop
        access elements of a list without the index
        variable that is the element is a copy of the thing in the list
        you can modify the copy, but the original is unchanged...
    for-i loop uses indices rather than elements
        does allow modification of the list
    """
    for word in my_words:
        word = 'happy'
        print(word)
    print(my_words)

    for index in range(len(my_words)):
        my_words[index] = 'radish'

    print(my_words)

    new_list = []
    for i in range(5):
        new_list.append(input('Tell me word: '))

    print(new_list)

    """
        All about range
        
        range(stop / end) = starts at 0 ends at stop - 1, end - 1 whichever you call it.
        range(start = 0, stop)
        
        range(0,0) = do nothing or empty list
        
        range(start=0, stop, step=1)
    """

    print(range(5))
    print(list(range(5)))
    print(list(range(14)))
    print(list(range(2, 18)))
    print(list(range(5, 12)))
    print(list(range(12, 5)))
    a = int(input('Tell me start: '))
    b = int(input('Tell me stop: '))
    for x in range(a, b):
        print(x)

    for y in []:
        print("I really like", y)

    print(list(range(2, 19, 3)))
    print(list(range(0, 100, 5)))

    print(list(range(12, 5, -1)))
    print(list(range(10, -1, -1)))
    print(list(range(100, 0, -7)))
    # also 'invalid'
    print(list(range(1, 10, -4)))

    for x in range(10, 50, 2):
        print(x / 10)

    the_list = ['a', 'b', 'c', 'd']
    # want new_list = ['d', 'c', 'b', 'a']
    new_list = []
    for i in range(len(the_list) - 1, -1, -1):
        print(the_list[i])
        new_list.append(the_list[i])
    print(new_list)

    yet_another_list = []
    for i in range(len(the_list)):
        yet_another_list.append(the_list[len(the_list) - 1 - i])
    print(yet_another_list)

    one_to_five = [1, 2, 3, 4, 5, ]
    # swap 2, 4
    # 2 is in position 1
    # 4 is in position 3

    temp_thing = one_to_five[3]
    one_to_five[3] = one_to_five[1]
    one_to_five[1] = temp_thing

    print(one_to_five)

    reverse_me = input('What to reverse? ')
    new_string = ''
    for i in range(len(reverse_me) - 1, -1, -1):
        # strings have indices just like lists
        new_string += reverse_me[i]
        # new_string = new_string + reverse_me[i]
    print(new_string)

    # you can read but not write
    # my_string = 'robot'
    # my_string[2] = 'c'
    # print(my_string)
    # Type Error

    """
    Draw a rectangle of asterisks
    """
    # normal
    print('*', end='\n')
    # new thing to do
    print('*', end='')
    # nothing in it, it still has end = '\n'
    print()

height = int(input('Height: '))
width = int(input('Width: '))

for y in range(height):
    for x in range(width):
        print('*', end='')
    print()

for y in range(1, height + 1):
    for x in range(y):
        print('*', end='')
    print()

radius = int(input('Radius: '))

for y in range(-1 * radius, radius + 1):
    for x in range(-1 * radius, radius + 1):
        if x ** 2 + y ** 2 <= radius ** 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()