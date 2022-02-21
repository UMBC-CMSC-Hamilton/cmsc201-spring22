"""
    What is a list?
        a ordered collection of elements.

        Way to access a list, using its index inside brackets.
"""
if False:
    my_list = [3, 2, 1, 6, 7, 8, 9]
    """
        Zeroth index
    """
    print(my_list[3])
    print(my_list[6])

    """
        for each loop, look at elements
        
        for-i loop where you look at indices
    """
    print('For each: ')
    for x in my_list:
        print(x)

    print('For i loop')
    """
    What is range(len(list))?
        range gives numbers starting at 0 goes up to num - 1
        range(num) -> 0, 1, 2, 3, 4, ... (num - 1)
        
        len(list) -> integer which is the length of the list
    """
    for i in range(len(my_list)):
        print(my_list[i])

    print(range(10))
    print(list(range(10)))

    """
        Range gives us the next number in a foor loop, 
            but doesn't always evaluate that number until it needs to.
    
    print(range(10000000000000000000000000000000))
    for x in range(10000000000000000000000000000000):
        print(x)
    """

    for x in [5, 4, 7, 2, 6, 8, 8, 2, 4, 7]:
        print(x)

    """
        Remember the difference between for each and for i
            for each loops give us elements of a list
                it doesn't matter what the element name is
            for i[ndex] loops give us indices
                use the variable as an index == for i
                i is a traditional name for an index variable
    """
    print(my_list)
    # for each loops make copies of the elements
    for x in my_list:
        x = x * 2  # x *= 2
        print(x, end=' ')
    print()

    print(my_list)

    for i in range(len(my_list)):
        my_list[i] *= 2
    print(my_list)


    my_new_list = []
    for i in range(3):
        my_new_list.append(input('Tell me something: '))

    print(my_new_list)

    """
        Let's talk about range a little more.
        
        range(num) -> 0, 1, 2,.... (num - 1)
    
        range(len(a_list_of_some_kind)) this will give us exactly the indices
    """
    problem = [1, 2, 3, 4, 5]
    print(len(problem))
    # IndexError
    # print(problem[5])

    """
        There is more to range than meets the eye...
        range(start, stop) (stop is required, start is defaulted to 0)
        
        range(start = 0, end)
        start, start + 1, start + 2, start + 3, ..., end - 1
    """

    for i in range(5, 11):
        print(i)

    print('Trying infinite range')
    for x in range(5, 1):
        print(x)

    # empty list because this range is invalid
    print(list(range(5, 1)))
    # these ranges work
    print(list(range(-11, -3)))
    print(list(range(-20, 5)))

    """
        range(start=0, stop, step=1)
    """

    print(list(range(2, 100, 5)))
    print(list(range(0, 100, 5)))
    # say you want to print out 100
    the_end = 100
    print(list(range(0, the_end + 1, 5)))

    print(list(range(10, 0, -1)))
    print(list(range(100, 0, -7)))
    print(list(range(5, 100, -1)))

"""
    Triangle time
"""

size = int(input('What is the size of the rectangle? '))

for i in range(size):
    for j in range(size):
        print((i, j), end=' ')
    print()


for i in range(size):
    for j in range(size):
        print('*', end=' ')
    print()

for i in range(size):
    for j in range(i + 1):
        print('*', end=' ')
    print()

print('\n\n\n')
for i in range(size):
    for j in range(size - i):
        print('*', end=' ')
    print()
print('\n\n\n')

for i in range(size):
    for j in range(size):
        if i >= j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

my_list = [2, 6, 4, 9, 1, 4, 2, 6, 4]

count = 0
for i in range(len(my_list)):
    for j in range(len(my_list)):
        if i != j and my_list[i] == my_list[j]:
            count += 1
            print(i, j)

print(f'The number of matches is {count // 2}')


for x in range(-1 * size, size + 1):
    for y in range(-1 * size, size + 1):
        if x ** 2 + y ** 2 <= size ** 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()