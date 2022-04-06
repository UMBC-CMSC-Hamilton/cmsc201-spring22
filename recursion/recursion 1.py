"""
    Recursion:
        Any process which can create copies of itself.
        
        A function which calls itself.

"""

def countdown(n):
    print(n)
    if n == 0:
        print('blastoff')
    else:
        countdown(n - 1)


countdown(10)


def palindrome(my_string):
    for i in range(len(my_string)):
        if my_string[i] != my_string[len(my_string) - 1 - i]:
            return False
        
    return True

def recursive_palindrome(my_string):
    print(my_string)
    if my_string:
        if my_string[0] == my_string[len(my_string) - 1]:

            the_slice= my_string[1: len(my_string) - 1]
            print('maybe a palindrome, check', the_slice)
            # this return is waiting on recursive_palindrome before it returns
            return recursive_palindrome(the_slice)
        else:
            print('definitely not a palindrome')
            return False
    else:
        print('empty string is a palindrome')
        return True
    
        
def factorial(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


def recursive_factorial(n):
    # base case, what stops the recursion
    if n == 0:
        return 1
    
    return n * recursive_factorial(n - 1)


def test_factorial():
    k = int(input('Enter an int: '))
    while k != -1:
        print(recursive_factorial(k))
        k = int(input('Enter an int: '))


def a_and_b(n, current_string):
    if n > 0:
        a_and_b(n - 1, current_string + 'a')
        a_and_b(n - 1, current_string + 'b')
    else:
        print(current_string)

# a_and_b(4, '')

def recursive_fib(n):
    if n > 1:
        return recursive_fib(n - 1) + recursive_fib(n - 2)
    else:
        return 1
    
def random_sequence(n):
    """
        5 a_{n - 1} + 4 a_{n - 2}
    :param n:
    :return:
    """
    if n > 2:
        return 7 * random_sequence(n - 1) - 2 * random_sequence(n - 3)
    elif n == 0:
        return 1
    elif n == 1:
        return 7
    elif n == 2:
        return 15
    else:
        return [1, 7, 15][n]


for i in range(40):
    print(i, recursive_fib(i))
