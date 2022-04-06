"""
    What is recursion?
        Any process that calls itself is a recursive process.
        
        GNU = GNU is Not Unix
            = GNU is Not Unix is Not Unix
            = GNU is Not Unix is Not Unix is Not Unix
        
        A function is recursive if it contains a function call to itself.
        
        In python there is a default, you can only run a recursive function
            1000 times within itself.
            
        What we need is a base case, a stopping point, a piece of code that
            ends our recursion`
"""


def countdown(n):
    if n == 0:
        print('blastoff')
    else:
        print('counting down from', n)
        countdown(n - 1)
        print('leaving', n)


def factorial(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


def rec_fact(n):
    if n <= 0:
        return 1
    
    return n * rec_fact(n - 1)


def test_factorial():
    the_int = int(input('Tell me int: '))
    while the_int != -1:
        print(factorial(the_int))
        the_int = int(input('Tell me int: '))


def rec_fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


def test_fib():
    for i in range(40):
        print(i, rec_fib(i))


def rec_pal(the_string):
    print(the_string)
    # base case
    if len(the_string) <= 1:
        return True
    
    # recursive case
    if the_string[0] == the_string[len(the_string) - 1]:
        return rec_pal(the_string[1: len(the_string) - 1])
    else:
        return False


def test_rec_pal():
    the_string = input('Tell me word: ')
    while the_string != 'quit':
        print(rec_pal(the_string))
        the_string = input('Tell me word: ')


def as_and_bs(n, current):
    print('\t' * n, 'The current is', current)
    if n == 0:
        print(current)
    else:
        as_and_bs(n - 1, current + 'a')
        as_and_bs(n - 1, current + 'b')

as_and_bs(5, '')

