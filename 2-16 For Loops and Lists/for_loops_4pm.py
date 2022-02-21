"""
Loops and lists

    Control Flow
        Sequential - Line by line execution
        Conditional - Branching behavior, you can choose the path that your
            program will follow.
        Iteration - repetition of a piece of code
"""
if False:
    for i in range(5):
        print(i)
    """
        range(int) will produce values from 0 up to but not including the endpoint
            range(5) will produce i = 0, 1, 2, 3, 4
            
        Gauss sum:
            1 + 2 + 3 + 4 + 5 + ... + n
    """

    n = int(input('What is n? '))
    total = 0
    for i in range(n + 1):
        total = total + i

    print(total)
    """
    1) print(total + n)
    2) total = total + i + 1 (the extra 1 shifts us up by one)
    3) for i in range(n + 1):
    
    1 + 2 + 3 + ... + n = n ( n + 1) // 2
    """

    my_string = input('Tell me a string: ')

    """
        When you put a string into a for loop as the "iterable object"
            it will give you character by character
    """
    for c in my_string:
        print(c)

    total_vowels = 0
    for c in my_string:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'y':
            total_vowels += 1
            # total_vowels = total_vowels + 1

    print(f'the number of vowels in {my_string} is {total_vowels}')

    """
        New data type: List
    """
    empty_list = []

    a_list = [1, 4, 5, 6, 9, 12, 11, 2, 1]
    float_list = [3.14, 2.718, 1.618, 0.577]
    string_list = ["hi", "this", "is", "a", "string", "list"]
    bool_list = [True, True, False, False, True, False, True, True]

    """
        These mixed type lists are allowed, but discouraged
    """
    random_list = [1, 2, 'hi', 3.1234, 'urban', 'cohort', True, False]

    """
        How do we use a for loop to scan these things?
    """

    for x in random_list:
        """
            Every time this for loop runs it picks the next element of the list.
        """
        print(x)

    test_list = ['aasdf', 'really', 'true', 'sandwich', 'quarter']
    print(test_list[0], test_list[2])
    """
    test_list[17] generates an IndexError
    """

    movie_list = []
    n = int(input('How many movies do you want to enter? '))
    for doesnt_matter in range(n):
        name_of_movie = input('Tell me movie name: ')
        movie_list.append(name_of_movie)
        print(movie_list)

    print('Its over: ')
    print(movie_list)

"""
    There is a function that will tell you the length of a list
    
    len(the_list_i_care_about) -> length
"""

b_list = [2, 5, 7, 4, 2, 5, 6, 7, 4, 3, 2, 6, 7, 4, 2, 2, 5, 7, 3, 2]
print(len(b_list))

print(len(input('Tell me string or movie name: ')))

"""
    Mutability - int float, string, bool are IMmutable (don't change)
    x is a copy not the original
    
    for each [element in the list] loop
"""
for x in b_list:
    print('start', x)
    x += 1
    print('end', x)
    """
    x is temporary its value is lost/ not saved back into the list
    """

print(b_list)

"""
    For each loops
        takes elements of the underlying string/list/whatever
    For i loops
        looks at indices
        traditionlly we use "i" as the most common index
"""
for index in range(len(b_list)):
    b_list[index] += 1
    # b_list[index] will change the element at "index"

print(b_list)

c_list = ['sea', 'ocean', 'water', 'boat', 'c is for cookie', 'titanic']
for i in range(len(c_list)):
    # index versus element
    # index = i, element = c_list[i]
    print(i, c_list[i])

a_list = [1, 2, 3, 9, 3, 5, 3, 5, 6, 4, 95, 7, 64, 4, 3, 76, 5, 33]
the_max = a_list[0]
"""
    Why are they elements and not indices?
    
    are you accessing a_list[x]?
    
    no we are not... if you dont stick the variable into a_list as an index
    in the brackets then it is probably an element
"""


for x in a_list:
    if x > the_max:
        the_max = x

print(f'The max is {the_max}')

max_pos = 0
for i in range(len(a_list)):
    if a_list[i] > a_list[max_pos]:
        max_pos = i

print(f'The max position is {max_pos} and the value is {a_list[max_pos]}')
