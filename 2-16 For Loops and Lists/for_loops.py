"""
    Control Flow
        Sequential - Execute line by line

        Conditional - Check an if statement

        Iterative/Iteration - repeat a bit of code multiple times.

"""
if False:
    n = int(input('What is n? '))

    running_total = 0

    """
        The idea behind range(5) is that its going to set i = 0 to start
            every time we loop its going to set i to the next number up
            1 -> 2 -> 3 -> 4 -> not 5
            
        if you want to go up to and include "n" then you should add one to n
            range(n + 1) 0, 1, 2, 3... , n (not including n + 1)
    """
    for i in range(n + 1):
        # running_total = running_total + i
        running_total += i
        print(i, running_total)

    print(running_total)


    the_string = input('Tell me a string please: ')
    count_a = 0
    for the_char in the_string:
        print(the_char)
        if the_char.lower() == 'a':
            count_a += 1
            # count_a = count_a + 1

    print(f'The total count is {count_a}')


    for num in [2, 17, 3, 1, 1, 4, 5]:
        print(num)

    """
        Lists are a new data type, but they basically contain other data
            including potentially other lists.. perhaps
    """
    the_list = [1, 2, 4, 8, 16]
    print(the_list)
    for x in the_list:
        print(x)
    """
    Lists can contain multiple types, but this should be avoided for reasons 
        not exactly python.  
    """
    my_random_list = [3, 4.2, 'hello', 5, 2, 'robot', True, []]
    print(my_random_list)
    for x in my_random_list:
        print(x)
    """
        you can use the index to get elements out of a list
    """
    print(my_random_list[4])
    print(my_random_list[5])
    print(my_random_list[2])

    """
        You can also assign a new element into a list by using the index
    """
    my_random_list[3] = 'candy'
    print(my_random_list)
    """
    make sure that the index is in the list when you do the assignment, otherwise
    you will get an IndexError.
    my_random_list[20] = 'Henry VIII'
    """

    empty_list = []
    print(empty_list)
    """
        An array has a fixed size (cannot change it) - no array in python
        List/vector can have a size change
    """
    my_list = []
    for i in range(5):
        x = input('Tell me a word: ')
        my_list.append(x)
        print(my_list)


    num_students = int(input('What is the number of students you want to add? '))
    student_list = []
    for num in range(num_students):
        student_list.append(input('Tell me a student name: '))

    print(student_list)

"""
    Lists have lengths
    
    len(some kind of list) -> will tell you the length
"""

my_list = [1, 2, 5, 7, 3, 5, 6, 3, 3, 5]
print(my_list)
print(len(my_list))

"""
    How do we loop but not through the elements, but through the indices?

    Combine len with range
    
    For-Each loops (for each element in the list)
        all the rest of them
        
    For-i loop, i = index 
    
"""
for index in range(len(my_list)):
    print(index, my_list[index])
