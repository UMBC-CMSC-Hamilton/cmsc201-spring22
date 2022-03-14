"""
    What is a function?
        sub-program
        way to run a given piece of code whenever you call the function

        inputs are called parameters, arguments
        output is the returned value

        when a function exits that is called a return

        y = f(x)

"""


def my_first_function():
    print('This is my first function.')


my_first_function()
my_first_function()
my_first_function()
my_first_function()


# this variable up here is called the parameter
def increment_me(x):
    print(x + 1)


# these things we plug into the function here are called arguments
increment_me(5)
increment_me(17)
increment_me(281)

"""
    Scope is the idea that inside functions we can create "local variables"
        local variable lives as long as the function lives
        whenever the function exits (returns) those variables that are not returned are "lost"
        the names of those variables are "forgotten"
"""


def add_together(x, y):
    return x + y


twelve = add_together(5, 7)
print(twelve)
print(add_together("sun", "roof"))


def get_input(lowest, highest):
    the_value = int(input(f'Tell me an integer between {lowest} and {highest}'))
    while the_value < lowest or the_value > highest:
        the_value = int(input(f'Tell me an integer between {lowest} and {highest}'))

    return the_value


# returned_value = get_input(1, 10)
# print(returned_value)

"""
    Why should you remove repetition in favor of functions?
        You know that it will always work the same way.
        If it has a bug, you only have to fix it in one place
        If it works, then its reliable anywhere you call it
"""

"""
    You can put loops into a function
"""

"""
    a prime is a number divisible by only 1 and itself

    is 1 prime? not according to the 1900-2022 definition
    
"""


def is_prime(the_number):
    if the_number <= 1:
        return False

    for i in range(2, the_number):
        if the_number % i == 0:
            return False

    return True


def get_primes(num):
    prime_list = []
    for x in range(num + 1):
        if is_prime(x):
            prime_list.append(x)
    return prime_list


def test_get_primes():
    num = int(input('Enter num: '))
    while num != 0:
        print(get_primes(num))
        num = int(input('Enter num: '))


""""
    Let's count the number of a's in a string
"""


def count_a(a_string):
    count = 0
    for char in a_string:
        if char == 'a':
            count += 1

    return count


def count_letter(a_string, the_letter):
    count = 0
    for char in a_string:
        if char == the_letter:
            count += 1

    return count


print(count_letter('once upon a time there were some cmsc201 students', 'a'))
print(count_letter('once upon a time there were some cmsc201 students', 'o'))
print(count_letter('once upon a time there were some cmsc201 students', 's'))


def is_palindrome(my_string):
    for i in range(len(my_string)):
        if my_string[i] != my_string[len(my_string) - 1 - i]:
            return False

    return True


def test_palindrome():
    #
    my_word = input('Tell me a palindrome: ')
    while my_word != 'quit':
        if is_palindrome(my_word):
            print(f'{my_word} is a palindrome')
        else:
            print(f'{my_word} is not a palindrome')
        my_word = input('Tell me a palindrome: ')

    return my_word


my_word = 'hello there i am a word'
my_other_word = test_palindrome()
print(my_word, my_other_word)

"""
    If you have a variable and return that variable, the value is what's being returned
    the name of the variable is local, so gets forgotten
"""


def return_x():
    x = 5
    return x


# this x is a new variable with "global scope" not local scope, it gets to live
# the previous x died.
x = return_x()
# NameError because x is gone (x was local)
# print(x, y)
print(x)

"""
Mutability

    4 basic data types (immutable)
        string, int, float, bool 
        
    other types (mutable)
        NoneType, list, dict, class
        
    if you pass a mutable object into a function, it can be changed by that function
        pass by reference - the actual object is accessible by the function
    but all immutable objects (basic data types) cannot be modified by a function
        pass by value - a copy of the value is made
        
"""

def append_me(the_list):
    the_list.append('me')


my_list = [1, 2, 3, 4, 5]
append_me(my_list)
print(my_list)


def increment_me(x):
    x = x + 1

the_int = 17
increment_me(17)
print(the_int)

